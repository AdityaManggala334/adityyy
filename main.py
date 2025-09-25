import json

# Buka file JSON
with open("AdityaManggalaPutra_V3925002.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Ambil bagian utama database
database = data["Database_System_Partisipasi_Rakyat_Konoha"]["Sumber_Data"]

# ---- Fungsi utilitas ----
def tampilkan_dataset_publik():
    print("\n=== Dataset Publik ===")
    for d in database["Dataset Publik"]:
        print(f"ID: {d['id_data']} | Nama: {d['nama_dataset']} | Tahun: {d['tahun']}")
        print(f"  Keterangan: {d['keterangan']}")

def tampilkan_portal_berita():
    print("\n=== Portal Berita Terverifikasi ===")
    for p in database["Portal Berita Terverifikasi"]:
        print(f"ID: {p['id_data']} | Portal: {p['portal']} | Judul: {p['judul_artikel']} | Tanggal: {p['tanggal']}")
        print(f"  Keterangan: {p['keterangan']}")

def tampilkan_lembaga_pengecek():
    print("\n=== Lembaga Pengecek Fakta ===")
    for l in database["Lembaga Pengecek Fakta"]:
        print(f"ID: {l['id_data']} | Lembaga: {l['lembaga']} | Judul: {l['judul_laporan']} | Tanggal: {l['tanggal']}")
        print(f"  Keterangan: {l['keterangan']}")

def tampilkan_data_sintetis():
    print("\n=== Data Sintetis ===")
    for s in database["Data Sintetis"]:
        print(f"ID: {s['id_data']} | Pewawancara: {s['pewawancara']} | Lokasi: {s['lokasi']} | Aktivitas: {s['aktivitas']}")
        print(f"  Keterangan: {s['keterangan']}")

# ---- Program Utama ----
if __name__ == "__main__":
    print("=== Database Sistem Partisipasi Rakyat Konoha ===")
    tampilkan_dataset_publik()
    tampilkan_portal_berita()
    tampilkan_lembaga_pengecek()
    tampilkan_data_sintetis()
