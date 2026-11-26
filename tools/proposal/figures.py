"""Black and white proposal figures with Indonesian labels.

Usage: python3 tools/proposal/figures.py OUT_DIR
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Ellipse, Circle, Rectangle
import sys, os

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
plt.rcParams["font.family"] = "DejaVu Sans"
FS = 9
LW = 1.2


def canvas(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, w * 10)
    ax.set_ylim(0, h * 10)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, t, dashed=False, round_=True, fs=FS, bold=False):
    st = "round,pad=0,rounding_size=1.2" if round_ else "square,pad=0"
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=st,
                                fc="white", ec="black", lw=LW,
                                ls=(0, (4, 3)) if dashed else "-"))
    ax.text(x, y, t, ha="center", va="center", fontsize=fs,
            fontweight="bold" if bold else "normal")
    return (x, y, w, h)


def term(ax, x, y, w, h, t):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle=f"round,pad=0,rounding_size={h/2}",
                                fc="white", ec="black", lw=LW))
    ax.text(x, y, t, ha="center", va="center", fontsize=FS)


def diamond(ax, x, y, w, h, t):
    ax.add_patch(Polygon([(x, y + h / 2), (x + w / 2, y), (x, y - h / 2), (x - w / 2, y)],
                         closed=True, fc="white", ec="black", lw=LW))
    ax.text(x, y, t, ha="center", va="center", fontsize=FS)


def cyl(ax, x, y, w, h, t, dashed=False):
    e = h * 0.18
    ls = (0, (4, 3)) if dashed else "-"
    ax.add_patch(Rectangle((x - w / 2, y - h / 2 + e / 2), w, h - e, fc="white", ec="none"))
    ax.plot([x - w / 2, x - w / 2], [y - h / 2 + e / 2, y + h / 2 - e / 2], "k", lw=LW, ls=ls)
    ax.plot([x + w / 2, x + w / 2], [y - h / 2 + e / 2, y + h / 2 - e / 2], "k", lw=LW, ls=ls)
    ax.add_patch(Ellipse((x, y - h / 2 + e / 2), w, e, fc="white", ec="black", lw=LW, ls=ls))
    ax.add_patch(Rectangle((x - w / 2 + 0.05, y - h / 2 + e / 2), w - 0.1, h - e, fc="white", ec="none"))
    ax.add_patch(Ellipse((x, y + h / 2 - e / 2), w, e, fc="white", ec="black", lw=LW, ls=ls))
    ax.text(x, y - e / 3, t, ha="center", va="center", fontsize=FS)


def arrow(ax, p, q, t=None, dashed=False, off=(0, 1.2), fs=FS - 1):
    ax.annotate("", xy=q, xytext=p,
                arrowprops=dict(arrowstyle="-|>", color="black", lw=LW,
                                ls=(0, (4, 3)) if dashed else "-", mutation_scale=11,
                                shrinkA=0, shrinkB=0))
    if t:
        ax.text((p[0] + q[0]) / 2 + off[0], (p[1] + q[1]) / 2 + off[1], t,
                ha="center", va="center", fontsize=fs, style="italic",
                bbox=dict(fc="white", ec="none", pad=0.5))


def poly(ax, pts, dashed=False):
    xs, ys = zip(*pts[:-1])
    ax.plot(xs, ys, "k", lw=LW, ls=(0, (4, 3)) if dashed else "-")
    arrow(ax, pts[-2], pts[-1], dashed=dashed)


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=300, bbox_inches="tight", pad_inches=0.05,
                facecolor="white")
    plt.close(fig)


# ---------- posisi: where the work sits ----------
fig, ax = canvas(6.4, 4.4)
for cx, cy, lab, lx, ly in [(24, 27, "Pengukuran\nRADAR\n(cabang A\nsampai C)", 18, 30),
                             (40, 27, "Rekam medis\n(RME)", 46, 31),
                             (32, 15, "EKG", 32, 7.5)]:
    ax.add_patch(Circle((cx, cy), 13, fc="none", ec="black", lw=LW))
    ax.text(lx, ly, lab, ha="center", va="center", fontsize=FS - 0.5)
ax.add_patch(Circle((32, 23.2), 3.6, fc="black", ec="black"))
ax.text(32, 23.2, "penelitian\nini", ha="center", va="center", fontsize=6.3, color="white",
        fontweight="bold")
ax.text(32, 41.5, "FHIR R4 (kompatibel SATUSEHAT) sebagai format bersama",
        ha="center", va="center", fontsize=FS - 1, style="italic")
save(fig, "posisi.png")

# ---------- alur: research flow ----------
fig, ax = canvas(5.2, 9.6)
X = 22
ys = [91, 80, 69, 58, 47, 34, 21, 10]
term(ax, X, ys[0], 24, 6, "Pertanyaan penelitian")
box(ax, X, ys[1], 30, 6.5, "Studi literatur\n(rantai argumen L1 sampai L8)")
box(ax, X, ys[2], 30, 6.5, "Kebutuhan\n(pembimbing, dokter, tim)")
box(ax, X, ys[3], 30, 6.5, "Spesifikasi rancangan")
box(ax, X, ys[4], 30, 6.5, "Pembangunan bertahap\n(uji lebih dulu)")
diamond(ax, X, ys[5], 22, 10, "Uji\nlolos?")
box(ax, X, ys[6], 30, 6.5, "Pengujian sistem\n(data cabang A sampai C)")
term(ax, X, ys[7], 24, 6, "Evaluasi dan laporan")
for a, b in [(0, 1), (1, 2), (2, 3), (3, 4)]:
    arrow(ax, (X, ys[a] - (3 if a == 0 else 3.25)), (X, ys[b] + 3.25))
arrow(ax, (X, ys[4] - 3.25), (X, ys[5] + 5))
arrow(ax, (X, ys[5] - 5), (X, ys[6] + 3.25), "ya", off=(2.5, 0))
arrow(ax, (X, ys[6] - 3.25), (X, ys[7] + 3))
poly(ax, [(X + 11, ys[5]), (44, ys[5]), (44, ys[4]), (X + 15, ys[4])])
ax.text(39, ys[5] + 1.5, "tidak", fontsize=FS - 1, style="italic")
poly(ax, [(X - 15, ys[6]), (2, ys[6]), (2, ys[1]), (X - 15, ys[1])], dashed=True)
ax.text(3.2, 50, "temuan baru", rotation=90, fontsize=FS - 1, style="italic", va="center")
save(fig, "alur.png")

# ---------- arsitektur: system architecture ----------
fig, ax = canvas(9.0, 5.4)
box(ax, 9, 44, 14, 6, "Sensor radar\nCW 24 GHz")
box(ax, 9, 30, 14, 6, "Papan\nAtomS3R")
box(ax, 33, 30, 18, 6, "Halaman Capture\n(peramban)")
box(ax, 58, 30, 18, 6, "Cloudflare\nWorker")
box(ax, 81, 30, 16, 6, "Server\nFHIR R4", bold=True)
cyl(ax, 81, 14, 12, 9, "Basis data")
box(ax, 81, 47, 16, 6, "Tampilan dokter\n(satu layar)", dashed=True)
box(ax, 49, 47, 16, 6, "Data cabang\nA sampai C", dashed=True)
box(ax, 49, 12, 16, 6, "RME\n(sintetis)", dashed=True)
arrow(ax, (9, 41), (9, 33), "I/Q", off=(3, 0))
arrow(ax, (16, 30), (24, 30), "USB", off=(0, 1.8))
arrow(ax, (42, 30), (49, 30), "HTTPS", off=(0, 1.8))
arrow(ax, (67, 30), (73, 30), "tunnel", off=(0, 1.8))
arrow(ax, (81, 27), (81, 18.5))
arrow(ax, (81, 33), (81, 44), "baca", off=(3, 0))
poly(ax, [(57, 47), (64, 47), (64, 36), (76, 36), (76, 33)], dashed=True)
ax.text(66.5, 41.5, "EKG, USG", fontsize=FS - 1, style="italic")
poly(ax, [(57, 12), (68, 12), (68, 24), (78, 24), (78, 27)], dashed=True)
ax.plot([52, 60], [3, 3], "k", lw=LW)
ax.text(61, 3, "sudah dibangun", va="center", fontsize=FS - 1)
ax.plot([76, 84], [3, 3], "k", lw=LW, ls=(0, (4, 3)))
ax.text(85, 3, "direncanakan", va="center", fontsize=FS - 1)
save(fig, "arsitektur.png")

# ---------- pengujian: test ladder ----------
fig, ax = canvas(9.6, 4.2)
labels = ["Uji unit dan\nintegrasi", "Simulator dengan\nnilai acuan", "Uji bangku\ndengan papan",
          "Uji ujung ke ujung\nlewat hosting", "Uji\ngangguan"]
xs = [9, 28, 47, 66, 85]
for i, (x, t) in enumerate(zip(xs, labels)):
    box(ax, x, 35, 16.5, 9, t)
    if i:
        arrow(ax, (xs[i - 1] + 8.25, 35), (x - 8.25, 35))
diamond(ax, 66, 20, 22, 8.5, "Kriteria\nterpenuhi?")
poly(ax, [(93.25, 35), (96, 35), (96, 20), (77, 20)])
poly(ax, [(55, 20), (9, 20), (9, 30.5)])
ax.text(32, 21.5, "tidak: perbaiki dan ulangi", ha="center", fontsize=FS - 1, style="italic")
term(ax, 66, 5, 30, 5.5, "Uji dengan data subjek")
arrow(ax, (66, 15.75), (66, 7.75), "ya", off=(3, 0))
save(fig, "pengujian.png")

# ---------- protokol: group protocol and handover ----------
fig, ax = canvas(6.6, 11.0)
X = 30
ax.add_patch(Rectangle((X - 28, 66), 56, 44, fc="none", ec="black", lw=LW, ls=(0, (2, 2))))
ax.text(X - 27, 108, "Protokol tim (etik bersama)", fontsize=FS - 1, style="italic", va="top")
term(ax, X, 101, 26, 5.6, "Persetujuan etik")
box(ax, X, 91, 30, 6.5, "Rekrutmen dan\npersetujuan subjek")
for xx, t in [(X - 17, "Radar\nCW 24 GHz"), (X, "EKG"), (X + 17, "USG\nmode A")]:
    box(ax, xx, 80, 14.5, 7, t)
box(ax, X, 70, 30, 5.6, "Data dianonimkan")
arrow(ax, (X, 101 - 2.8), (X, 91 + 3.25))
ax.plot([X, X], [91 - 3.25, 86], "k", lw=LW)
ax.plot([X - 17, X + 17], [86, 86], "k", lw=LW)
ax.plot([X - 17, X + 17], [74.5, 74.5], "k", lw=LW)
for xx in (X - 17, X, X + 17):
    arrow(ax, (xx, 86), (xx, 80 + 3.5))
    ax.plot([xx, xx], [80 - 3.5, 74.5], "k", lw=LW)
arrow(ax, (X, 74.5), (X, 70 + 2.8))
box(ax, X, 55, 30, 6.5, "Penerimaan data\noleh sistem")
arrow(ax, (X, 70 - 2.8), (X, 55 + 3.25), "cabang D", off=(6, 0))
diamond(ax, X, 41, 26, 10, "Lengkap dan\nselaras?")
arrow(ax, (X, 55 - 3.25), (X, 41 + 5))
box(ax, X, 27, 30, 5.6, "Tampilan dokter")
arrow(ax, (X, 41 - 5), (X, 27 + 2.8), "ya", off=(3, 0))
term(ax, X, 16, 26, 5.6, "Simpan di laptop")
arrow(ax, (X, 27 - 2.8), (X, 16 + 2.8))
poly(ax, [(X + 13, 41), (X + 31, 41), (X + 31, 70), (X + 15, 70)])
ax.text(X + 22, 43, "tidak:\nkembalikan ke tim", ha="center", va="bottom", fontsize=FS - 1.5,
        style="italic")
ax.set_ylim(11, 111)
save(fig, "protokol.png")
# ---------- helpers for use case and sequence figures ----------
def actor(ax, x, y, t):
    ax.add_patch(Circle((x, y + 4.2), 1.3, fc="white", ec="black", lw=LW))
    ax.plot([x, x], [y + 2.9, y + 0.2], "k", lw=LW)
    ax.plot([x - 2, x + 2], [y + 2.1, y + 2.1], "k", lw=LW)
    ax.plot([x, x - 1.6], [y + 0.2, y - 2.2], "k", lw=LW)
    ax.plot([x, x + 1.6], [y + 0.2, y - 2.2], "k", lw=LW)
    ax.text(x, y - 3.6, t, ha="center", va="top", fontsize=FS)


def usecase(ax, x, y, t, dashed=False):
    ax.add_patch(Ellipse((x, y), 27, 6.2, fc="white", ec="black", lw=LW,
                         ls=(0, (4, 3)) if dashed else "-"))
    ax.text(x, y, t, ha="center", va="center", fontsize=FS - 1)


def link(ax, p, q, dashed=False):
    ax.plot([p[0], q[0]], [p[1], q[1]], "k", lw=0.9, ls=(0, (4, 3)) if dashed else "-")


def lifelines(ax, names, xs, top, bottom, dashed=False):
    for n, x in zip(names, xs):
        box(ax, x, top, 13.5, 5.6, n, fs=FS - 1, dashed=dashed)
        ax.plot([x, x], [top - 2.8, bottom], "k", lw=0.8, ls=(0, (2, 2)))


def msg(ax, x1, x2, y, t, ret=False, dashed=False):
    if x1 == x2:
        ax.plot([x1, x1 + 3, x1 + 3], [y + 1, y + 1, y - 1], "k", lw=LW)
        arrow(ax, (x1 + 3, y - 1), (x1, y - 1))
        ax.text(x1 + 4, y, t, ha="left", va="center", fontsize=FS - 1.5, style="italic",
                bbox=dict(fc="white", ec="none", pad=0.3), zorder=5)
        return
    arrow(ax, (x1, y), (x2, y), dashed=ret or dashed)
    ax.text((x1 + x2) / 2, y + 1.3, t, ha="center", va="center", fontsize=FS - 1.5,
            style="italic", bbox=dict(fc="white", ec="none", pad=0.3))


# ---------- usecase: actors and functions ----------
fig, ax = canvas(9.0, 8.4)
ax.add_patch(Rectangle((19, 4), 52, 76, fc="none", ec="black", lw=LW))
ax.text(45, 77.5, "Sistem PRATA", ha="center", va="center", fontsize=FS, fontweight="bold")
uc = {
    "papan": (45, 71, "Daftarkan papan radar"),
    "pasien": (45, 63, "Buat pasien uji"),
    "sesi": (45, 55, "Buka dan tutup sesi"),
    "rekam": (45, 47, "Pratinjau dan rekam\n(halaman Capture)"),
    "kirim": (45, 39, "Kirim potongan sinyal\nke sesi terbuka"),
    "review": (45, 31, "Tinjau rekaman\n(halaman Review)"),
    "terpadu": (45, 23, "Lihat tampilan terpadu\n(direncanakan)"),
    "baca": (45, 15, "Baca rekaman sendiri"),
    "bagi": (45, 8, "Simpan dan bagikan data\n(belum ditetapkan)"),
}
for k, (x, y, t) in uc.items():
    usecase(ax, x, y, t, dashed=k in ("terpadu", "bagi"))
actor(ax, 8, 62, "Admin")
actor(ax, 8, 32, "Dokter")
actor(ax, 82, 42, "Papan radar")
actor(ax, 82, 12, "Pasien")
for k in ("papan", "pasien", "sesi", "review"):
    link(ax, (10.5, 64), (31.5, uc[k][1]))
for k in ("sesi", "rekam", "review"):
    link(ax, (10.5, 34), (31.5, uc[k][1]))
link(ax, (10.5, 34), (31.5, uc["terpadu"][1]), dashed=True)
link(ax, (79.5, 44), (58.5, uc["kirim"][1]))
link(ax, (79.5, 14), (58.5, uc["baca"][1]))
link(ax, (79.5, 14), (58.5, uc["bagi"][1]), dashed=True)
ax.text(8, 82, "Akun dibuat di laptop,\ndi luar sistem web", ha="center", va="center",
        fontsize=FS - 1.5, style="italic")
save(fig, "usecase.png")

# ---------- seq_sesi: open a session and record (built) ----------
fig, ax = canvas(10.0, 9.2)
names = ["Dokter\natau admin", "Halaman\nSessions", "Halaman\nCapture", "Papan\nradar", "Server\nFHIR R4", "Basis\ndata"]
xs = [8, 24, 41, 58, 75, 92]
lifelines(ax, names, xs, 87, 3)
rows = [
    (0, 1, "buka sesi (pasien, papan)"),
    (1, 4, "buat sesi"),
    (4, 5, "simpan Encounter"),
    (2, 3, "BOARD?"),
    (3, 2, "ID chip dan kunci", True),
    (2, 4, "minta sesi papan (kunci)"),
    (4, 2, "pasien dan Encounter", True),
    (2, 2, "pratinjau, lalu Rekam"),
    (3, 2, "100 sampel per detik", True),
    (2, 2, "potongan 10 detik\nmasuk kotak keluar"),
    (2, 4, "kirim Observation (bersyarat)"),
    (4, 4, "cek peran, sesi, validasi"),
    (4, 5, "simpan Observation"),
    (4, 2, "201 Created", True),
    (2, 2, "hapus salinan lokal"),
    (0, 1, "tutup sesi"),
    (1, 4, "akhiri Encounter"),
]
y = 79
for r in rows:
    a, b, t = r[0], r[1], r[2]
    msg(ax, xs[a], xs[b], y, t, ret=len(r) > 3)
    y -= 4.4
save(fig, "seq_sesi.png")

# ---------- seq_dokter: integrated review (planned) ----------
fig, ax = canvas(9.0, 5.6)
names = ["Dokter", "Tampilan\nterpadu", "Server\nFHIR R4"]
xs = [12, 45, 78]
lifelines(ax, names, xs, 51, 3, dashed=True)
ax.text(45, 57, "Seluruh alur direncanakan, belum dibangun", ha="center", va="center",
        fontsize=FS - 1, style="italic")
rows = [
    (0, 1, "pilih pasien dan kunjungan"),
    (1, 2, "ambil data RME sintetis"),
    (1, 2, "ambil Observation radar"),
    (1, 2, "ambil rekaman EKG"),
    (2, 1, "resource FHIR", True),
    (1, 1, "selaraskan pada\nsatu sumbu waktu"),
    (1, 0, "tampilkan dalam satu layar", True),
    (0, 0, "dokter menimbang\ndan memutuskan"),
]
y = 43
for r in rows:
    msg(ax, xs[r[0]], xs[r[1]], y, r[2], ret=len(r) > 3, dashed=True)
    y -= 5
save(fig, "seq_dokter.png")

print("ok")
