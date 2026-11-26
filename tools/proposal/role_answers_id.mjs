// Indonesian research-role answers, in the layout of
// docs/proposal_guide/proposal_questions_template/template.docx.
// Usage: node tools/proposal/role_answers_id.mjs OUT.docx
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType } from "docx";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const FIG = path.join(ROOT, "docs/proposal_md/figures");
const TNR = "Times New Roman";
const SP = { before: 240, after: 240, line: 276 };

const center = (t) => new Paragraph({ alignment: AlignmentType.CENTER, spacing: SP,
  children: [new TextRun({ text: t, bold: true, font: TNR, size: 24 })] });
const q = (t) => new Paragraph({ spacing: SP, keepNext: true,
  children: [new TextRun({ text: t, bold: true, font: TNR, size: 24 })] });
const p = (t) => new Paragraph({ spacing: SP, alignment: AlignmentType.JUSTIFIED,
  children: [new TextRun({ text: t, font: TNR, size: 24 })] });

function fig(file, widthIn, caption) {
  const buf = fs.readFileSync(path.join(FIG, file));
  const w = buf.readUInt32BE(16), h = buf.readUInt32BE(20);
  const W = Math.round(widthIn * 96), H = Math.round(W * h / w);
  return [
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 240, after: 60 }, keepNext: true,
      children: [new ImageRun({ type: "png", data: buf, transformation: { width: W, height: H },
        altText: { title: caption, description: caption, name: file } })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 240 },
      children: [new TextRun({ text: caption, italics: true, font: TNR, size: 20 })] }),
  ];
}

export const body = () => [
  center("Daffa Atharuna Rijadi"),
  center("5023231024"),
  new Paragraph({ spacing: SP, children: [] }),

  q("Peran dan kegiatan dalam kelompok riset"),
  p("Penelitian ini merupakan cabang D dari satu pohon penelitian kelompok riset Teknik Biomedik ITS bersama RSUD Dr. Soetomo, dengan pembimbing Rezki El Arif, S.T., M.T., Ph.D. dan dokter mitra dr. Ruth Irena Gunadi, Sp.JP, FIHA. Seluruh cabang memakai platform radar continuous wave (CW) 24 GHz yang sama. Cabang A merekam morfologi pulsa karotis pada irama normal dan aritmia dengan EKG sebagai acuan waktu, cabang B menilai asimetri pulsa karotis kiri dan kanan pada penyakit arteri koroner, dan cabang C mengestimasi denyut vena jugularis (jugular venous pulse, JVP) dengan ultrasound mode A sebagai acuan. Fokus utama cabang D adalah sistem informasi yang menerima hasil pengukuran ketiga cabang tersebut, menyimpannya bersama rekam medis elektronik (RME) dan rekaman EKG dalam format FHIR R4 yang kompatibel dengan SATUSEHAT, lalu menampilkannya kepada dokter dalam satu tampilan. Judul penelitian adalah \"Pengembangan Sistem Pendukung Keputusan Klinis Berbasis Interoperabilitas Data Rekam Medis Elektronik dan Pengukuran Kardiovaskular RADAR\"."),
  p("Kegiatan yang telah dilakukan dan dokumen buktinya adalah sebagai berikut. Pertama, penyusunan proposal etik kelompok, yang mencantumkan cabang D sebagai penyusun format FHIR untuk keluaran radar dengan memakai ulang data cabang A sampai C. Kedua, penyusunan proposal tugas akhir yang memuat abstrak, Bab I, Bab II dengan 41 rujukan, dan Bab III Metodologi. Ketiga, studi literatur yang disusun sebagai rantai argumen delapan mata rantai, disertai diagram fishbone dan katalog yang menghubungkan setiap klaim dengan sumbernya. Keempat, konsultasi pada 15 Oktober 2026 dengan pembimbing dan dokter RSUD Dr. Soetomo untuk menyepakati lokasi pengambilan data, peran ultrasound sebagai acuan, dan pembagian topik. Kelima, pembangunan purwarupa yang terdiri atas firmware papan radar, halaman web penangkap sinyal mentah, server FHIR R4, dan versi publik situs di Cloudflare. Per 24 November 2026, purwarupa lolos 236 uji server, 179 uji halaman web, dan 23 uji lapisan hosting."),

  q("a). Bagaimana memastikan bahwa ide penelitian Anda berbeda dan memiliki kontribusi ilmiah dan praktis yang signifikan."),
  p("Keunikan ide dipastikan melalui tiga langkah. Langkah pertama adalah pemetaan literatur. Argumen penelitian dipecah menjadi delapan klaim, yaitu beban rawat ulang gagal jantung, kongesti sisa sebagai pemicu rawat ulang, informasi pada fitur gelombang JVP, nilai satu kali pengukuran, keterbatasan pemeriksaan JVP di sisi tempat tidur, kemampuan radar, kebutuhan akan konteks pasien, dan manfaat tampilan terpadu bagi dokter. Setiap klaim ditelusuri secara terpisah sehingga kekuatan dan kelemahan setiap mata rantai terlihat. Dalam penelusuran tersebut tidak ditemukan sistem yang menggabungkan JVP dari radar dengan RME dan EKG dalam satu tampilan klinis. Langkah kedua adalah pembatasan lingkup terhadap cabang lain. Perangkat radar, akuisisi sinyal, dan algoritma pengolahan sinyal berada pada cabang A sampai C, sedangkan cabang D hanya mengerjakan sistem setelah hasil pengukuran tersedia, sehingga tidak ada tumpang tindih. Langkah ketiga adalah penyesuaian arah berdasarkan masukan pembimbing. Rancangan awal berupa profil FHIR untuk perangkat radar diperluas menjadi sistem pendukung keputusan klinis, karena satu hasil pengukuran baru bermakna bila dibaca bersama konteks pasien. Proposal etik kelompok masih menuliskan cabang D sebagai penyusunan profil FHIR, sehingga perluasan cakupan ini perlu dicantumkan dalam pembaruan proposal etik."),
  ...fig("posisi.png", 4.2, "Gambar 1. Posisi penelitian ini"),
  p("Kontribusi ilmiah penelitian ini adalah pola integrasi data dari perangkat pengukuran baru ke rekam medis berbasis standar. Sinyal in phase dan quadrature (I/Q) radar belum memiliki kode standar, sehingga penelitian ini menetapkan cara menyimpannya sebagai FHIR Observation di samping EKG dan data RME, serta mencatat bagian standar yang belum mencukupi. Kontribusi praktisnya adalah satu tampilan bagi dokter yang memuat gelombang radar, EKG, dan rekam medis pasien pada satu sumbu waktu, sehingga dokter tidak perlu membuka beberapa sistem. Kebutuhan ini relevan bagi fasilitas kesehatan di Indonesia, yang menurut survei menjalankan sekitar 30 sistem informasi per Puskesmas dengan sekitar separuhnya menuntut entri data berulang. Batas klaimnya ditetapkan sejak awal: sistem bukan alat diagnosis, tidak menghasilkan prediksi maupun skor risiko, dan tidak menyumbang algoritma pengolahan sinyal. Keputusan klinis tetap berada pada dokter."),

  q("b). Bagaimana merancang \"metodologi\" yang rinci dari tema yang Anda usulkan."),
  p("Metodologi disusun sebagai siklus rekayasa sistem dengan tahapan berikut. Tahap 1 adalah perumusan pertanyaan penelitian. Tahap 2 adalah studi literatur berbasis rantai argumen L1 sampai L8. Tahap 3 adalah penggalian kebutuhan dari pembimbing, dokter mitra, dan cabang A sampai C sebagai penyedia data. Tahap 4 adalah penulisan spesifikasi rancangan untuk setiap bagian sistem, yang memuat tujuan, batas lingkup, keputusan rancangan beserta alasannya, dan syarat selesai. Tahap 5 adalah pembangunan bertahap dengan pengujian yang ditulis sebelum kode yang diujinya. Tahap 6 adalah pengujian berjenjang. Bila suatu uji gagal, proses kembali ke tahap 5, dan bila pengujian menghasilkan temuan baru, proses kembali ke tahap 2 dan 3."),
  ...fig("alur.png", 3.2, "Gambar 2. Alur penelitian"),
  p("Sistem dirancang dalam lima lapisan yang dapat dibangun dan diuji terpisah. Lapisan akuisisi adalah modul radar CW 24 GHz pada papan mikrokontroler AtomS3R yang mengambil sampel kanal I dan Q sebanyak 100 kali per detik dari pewaktu perangkat keras, dengan nomor urut pada setiap sampel agar waktu yang hilang tercatat sebagai celah. Lapisan penangkapan adalah halaman web yang membaca papan melalui peramban, mengelompokkan sampel menjadi potongan paling lama 10 detik, menyimpannya di peramban, dan menghapusnya hanya setelah server mengonfirmasi penyimpanan. Lapisan data adalah server FHIR R4 yang menyimpan pasien, dokter, kunjungan, perangkat, dan hasil pengukuran sebagai resource standar serta menolak data tidak valid dengan laporan galat bergaya SATUSEHAT. Lapisan akses membatasi hak setiap peran: admin mendaftarkan papan dan pasien uji, dokter membuka sesi pengukuran, papan hanya menulis ke sesinya sendiri yang terbuka, dan pasien hanya membaca rekamannya sendiri. Lapisan hosting adalah Cloudflare Worker yang meneruskan permintaan ke server lokal, sehingga data tetap tersimpan di laptop peneliti. Lapisan berikutnya yang direncanakan adalah penerimaan data cabang A sampai C, impor RME sintetis, dan tampilan terpadu bagi dokter."),
  ...fig("arsitektur.png", 6.0, "Gambar 3. Arsitektur sistem"),
  p("Setiap keputusan metode memakai kriteria yang ditetapkan sebelum pengujian. Contohnya adalah pemilihan cara menampilkan gelombang radar. Rekaman sintetis dengan gerakan yang diketahui dibuat lebih dulu, enam metode kandidat dijalankan, dan skor setiap metode dihitung dari kedekatan keluarannya dengan nilai sebenarnya. Aturan pemilihan ditulis sebelum metode dijalankan. Metode hybrid terpilih dengan median skor 0,92, dan delapan sampel skor dihitung ulang secara independen dengan hasil yang cocok. Pilihan ini hanya untuk keperluan tampilan dan tidak diposisikan sebagai pengukuran."),

  q("c). Jelaskan perencanaan Anda untuk (1) metode eksperimen perangkat keras dan atau perangkat lunak yang dirancang (2) eksperimen dengan subjek manusia"),
  q("(1) Metode eksperimen perangkat keras dan perangkat lunak"),
  p("Pengujian dilakukan dalam lima jenjang, dan jenjang berikutnya hanya dijalankan bila jenjang sebelumnya lolos. Jenjang 1 adalah uji unit dan integrasi otomatis untuk server, halaman web, lapisan hosting, dan logika firmware. Jenjang 2 adalah uji dengan papan simulasi yang menghasilkan sinyal dengan nilai acuan, untuk memastikan setiap sampel tiba di basis data tanpa berubah. Jenjang 3 adalah uji bangku dengan papan nyata. Hasil saat ini menunjukkan kedua kanal berada di sekitar 1,53 V dengan sebaran sekitar 1 mV saat diam, dan sebaran naik menjadi 90 sampai 170 mV ketika ada gerakan di depan radar, sehingga radar terbukti merespons gerakan, meskipun rekaman ini belum ditinjau sebagai sinyal fisiologis. Jenjang 4 adalah uji ujung ke ujung melalui alamat hosting. Jenjang 5 adalah uji gangguan, misalnya menghentikan server di tengah perekaman. Pada uji ini seluruh potongan yang tertahan di peramban terunggah 16 sampai 17 detik setelah server kembali menyala tanpa duplikasi."),
  ...fig("pengujian.png", 6.0, "Gambar 4. Jenjang pengujian perangkat keras dan perangkat lunak"),
  p("Kriteria keberhasilan yang dipakai adalah sebagai berikut. Keutuhan data terpenuhi bila jumlah sampel yang tersimpan sama dengan jumlah yang dikirim, tanpa duplikasi, dengan celah tercatat. Interoperabilitas terpenuhi bila setiap resource lolos validasi FHIR R4, dan kelengkapan pemetaan EKG serta RME dihitung sebagai persentase variabel wajib yang berhasil dipetakan. Penyelarasan waktu terpenuhi bila rekaman radar dan EKG yang diambil bersamaan sejajar dalam toleransi yang ditetapkan sebelum pengujian. Kinerja hosting diukur dari waktu proses Cloudflare Worker, yang saat ini tidak lebih dari 3 ms per permintaan. Hal yang belum terverifikasi adalah uji papan nyata melalui alamat publik dan urutan kanal I dan Q pada papan."),

  q("(2) Eksperimen dengan subjek manusia"),
  p("Pengambilan data subjek dijalankan oleh cabang A sampai C sebagai satu protokol bersama di poliklinik RSUD Dr. Soetomo, di bawah satu proposal etik kelompok. Urutan prosedurnya adalah sebagai berikut. Langkah 1 adalah memperoleh persetujuan komite etik penelitian kesehatan rumah sakit, karena tidak ada pengambilan data sebelum persetujuan keluar. Langkah 2 adalah rekrutmen dan penyaringan subjek menurut kriteria inklusi dan eksklusi, serta prosedur persetujuan subjek, yang keduanya akan ditetapkan dalam bagian metode proposal etik. Langkah 3 adalah perekaman: radar CW 24 GHz merekam leher tanpa menyentuh kulit, cabang A merekam EKG sebagai acuan waktu, dan cabang C memakai ultrasound mode A sebagai acuan JVP. Ketiga pemeriksaan itu noninvasif, dan penilaian risiko resminya menunggu bagian risiko pada proposal etik. Jumlah sekitar 100 subjek dalam waktu lebih dari satu bulan telah dibahas bersama dokter, dengan angka final ditetapkan dalam protokol etik."),
  p("Cabang D tidak menambah subjek maupun prosedur dan memakai ulang data cabang A sampai C, dengan usulan agar data dianonimkan sebelum diserahkan. Syarat anonimisasi ini perlu ditambahkan ke proposal etik. Prosedur penerimaan data oleh sistem, yang masih direncanakan, adalah sebagai berikut. Langkah 4 adalah penerimaan rekaman radar, EKG, dan nilai acuan ultrasound dari setiap cabang. Langkah 5 adalah pemeriksaan kelengkapan sampel, penyelarasan radar dan EKG pada satu sumbu waktu, dan pemeriksaan sensor gerak untuk menandai rekaman dengan gerakan subjek. Langkah 6 adalah pengembalian rekaman yang tidak lolos ke cabang terkait. Langkah 7 adalah penampilan rekaman yang lolos kepada dokter dalam satu tampilan, dengan seluruh data disimpan hanya di laptop peneliti. Data RME nyata memerlukan persetujuan etik tersendiri, sehingga evaluasi bagian RME memakai rekam medis sintetis, dan sistem tidak diklaim tervalidasi secara klinis melalui eksperimen ini."),
  ...fig("protokol.png", 3.6, "Gambar 5. Protokol pengambilan data kelompok dan penerimaan data oleh sistem"),
];

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const out = process.argv[2];
  const doc = new Document({
    styles: { default: { document: { run: { font: TNR, size: 24 } } } },
    sections: [{ properties: { page: { size: { width: 11909, height: 16834 },
      margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } }, children: body() }],
  });
  fs.writeFileSync(out, await Packer.toBuffer(doc));
  console.log("wrote", out);
}
