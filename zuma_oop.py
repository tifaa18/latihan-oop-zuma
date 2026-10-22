class KatakZuma:
    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True
        
    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru
        self.load_gambar(warna_baru)
        
    def load_gambar(self, warna):
        pass

    def tembak(self):
        self.skor += 50
        print(f"Katak menembak bola! Skor bertambah +50.")

    def info_status(self):
        print("=== STATUS KATAK ZUMA ===")
        print(f"Warna Peluru saat ini : {self.warna_peluru}")
        print(f"Total Skor pemain     : {self.skor}")
        print(f"Status Aktif          : {self.is_active}")
        print("=========================\n")


# --- UJI COBA PROGRAM ---
# 1. Implementasi Objek (Instansiasi) menggunakan nama variabel katak_player sesuai instruksi
katak_player = KatakZuma("Kuning")

# 2. Panggil behavior info_status() untuk melihat kondisi awal objek
print("--- Kondisi Awal ---")
katak_player.info_status()

# 3. Lakukan pengubahan properties warna dengan memanggil ganti_warna("Merah")
print("Melakukan perubahan warna...")
katak_player.ganti_warna("Merah")

# 4. Panggil behavior tembak() untuk menambah skor
katak_player.tembak()

# 5. Panggil kembali info_status() untuk membuktikan properties berhasil berubah
print("--- Kondisi Akhir ---")
katak_player.info_status()