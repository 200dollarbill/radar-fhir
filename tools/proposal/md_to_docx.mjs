// Markdown (the subset proposal.md uses) to Word, in the proposal layout.
// Usage: node tools/proposal/md_to_docx.mjs IN.md OUT.docx
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType, Table, TableRow,
  TableCell, WidthType, BorderStyle,
} from "docx";

const TNR = "Times New Roman";
const PAGE_W = 11909, MARGIN = 1440, CONTENT_W = PAGE_W - 2 * MARGIN;
const SP = { before: 240, after: 240, line: 276 };
const STOP = /^Catatan untuk Mahasiswa\s*$/;

export function parseBlocks(md) {
  const lines = md.replace(/<!--[\s\S]*?-->/g, "").split("\n");
  const blocks = [];
  let inBib = false;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trimEnd();
    if (STOP.test(line.trim())) break;
    if (!line.trim() || /^---+$/.test(line.trim())) continue;
    const h = line.match(/^(#{1,3})\s+(.*)$/);
    if (h) {
      inBib = /DAFTAR PUSTAKA/i.test(h[2]);
      blocks.push({ kind: "heading", level: h[1].length, text: h[2] });
      continue;
    }
    const img = line.match(/^!\[([^\]]*)\]\(([^)]+)\)$/);
    if (img) { blocks.push({ kind: "image", caption: img[1], src: img[2] }); continue; }
    if (line.startsWith("|")) {
      const rows = [];
      for (; i < lines.length && lines[i].startsWith("|"); i++) {
        const cells = lines[i].trim().replace(/^\||\|$/g, "").split("|").map((c) => c.trim());
        if (cells.every((c) => /^:?-+:?$/.test(c))) continue;
        rows.push(cells);
      }
      i--;
      blocks.push({ kind: "table", rows });
      continue;
    }
    blocks.push({ kind: inBib ? "bib" : "para", text: line.trim() });
  }
  return blocks;
}

function runs(text, opts = {}) {
  const out = [];
  for (const part of text.split(/(\*\*[^*]+\*\*|\*[^*]+\*)/)) {
    if (!part) continue;
    const bold = part.startsWith("**"), ital = !bold && part.startsWith("*") && part.length > 2;
    const t = bold ? part.slice(2, -2) : ital ? part.slice(1, -1) : part;
    out.push(new TextRun({ text: t, font: TNR, size: opts.size ?? 24, bold: bold || opts.bold,
      italics: ital || opts.italics }));
  }
  return out;
}

function pngSize(buf) { return [buf.readUInt32BE(16), buf.readUInt32BE(20)]; }

export async function mdToDocx(md, baseDir) {
  const children = [];
  let afterJudul = false;
  for (const b of parseBlocks(md)) {
    if (afterJudul && b.kind === "para") {
      afterJudul = false;
      children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: SP,
        children: runs(b.text, { bold: true, size: 26 }) }));
      continue;
    }
    if (b.kind === "heading") {
      const top = b.level <= 2;
      const center = b.level === 1 || /^(BAB |ABSTRAK|DAFTAR PUSTAKA)/.test(b.text);
      if (b.text === "Judul:") { afterJudul = true; continue; }
      children.push(new Paragraph({ alignment: center ? AlignmentType.CENTER : AlignmentType.LEFT,
        spacing: SP, keepNext: true, pageBreakBefore: /^(BAB |DAFTAR PUSTAKA)/.test(b.text),
        children: runs(b.text, { bold: true, size: top ? 28 : 24 }) }));
    } else if (b.kind === "image") {
      const file = path.resolve(baseDir, b.src);
      if (!fs.existsSync(file)) throw new Error(`image not found: ${b.src}`);
      const buf = fs.readFileSync(file);
      const [w, h] = pngSize(buf);
      const maxW = 6 * 96, maxH = 7.5 * 96;
      let W = Math.min(maxW, w), H = Math.round(W * h / w);
      if (H > maxH) { H = maxH; W = Math.round(H * w / h); }
      children.push(new Paragraph({ alignment: AlignmentType.CENTER, keepNext: true,
        spacing: { before: 240, after: 60 },
        children: [new ImageRun({ type: "png", data: buf, transformation: { width: W, height: H },
          altText: { title: b.caption, description: b.caption, name: path.basename(b.src) } })] }));
      children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 240 },
        children: runs(b.caption, { italics: true, size: 20 }) }));
    } else if (b.kind === "table") {
      const n = b.rows[0].length, colW = Math.floor(CONTENT_W / n);
      const border = { style: BorderStyle.SINGLE, size: 4, color: "000000" };
      const borders = { top: border, bottom: border, left: border, right: border };
      children.push(new Table({
        width: { size: colW * n, type: WidthType.DXA },
        columnWidths: Array(n).fill(colW),
        rows: b.rows.map((r, ri) => new TableRow({ children: r.map((c) => new TableCell({
          width: { size: colW, type: WidthType.DXA }, borders,
          margins: { top: 60, bottom: 60, left: 100, right: 100 },
          children: [new Paragraph({ children: runs(c, { bold: ri === 0, size: 22 }) })] })) })),
      }));
      children.push(new Paragraph({ spacing: { before: 0, after: 120 }, children: [] }));
    } else if (b.kind === "bib") {
      children.push(new Paragraph({ spacing: { before: 0, after: 120, line: 240 },
        indent: { left: 567, hanging: 567 }, children: runs(b.text, { size: 22 }) }));
    } else {
      children.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: SP,
        indent: { firstLine: 567 }, children: runs(b.text) }));
    }
  }
  const doc = new Document({
    styles: { default: { document: { run: { font: TNR, size: 24 } } } },
    sections: [{ properties: { page: { size: { width: PAGE_W, height: 16834 },
      margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } } }, children }],
  });
  return Packer.toBuffer(doc);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const [inp, out] = process.argv.slice(2);
  const buf = await mdToDocx(fs.readFileSync(inp, "utf8"), path.dirname(path.resolve(inp)));
  fs.writeFileSync(out, buf);
  console.log("wrote", out);
}
