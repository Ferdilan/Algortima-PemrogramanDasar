import math

class Lingkaran:
    def keliling(self, r):
        hasil = 2 * math.pi * r
        return hasil

    def luas(self, r):
        hasil = math.pi * r ** 2
        return hasil

# Membuat objek dari kelas Lingkaran
lingkaran = Lingkaran()

# Input dari user untuk jari-jari lingkaran
jari_jari = int(input("Masukkan jari-jari lingkaran: "))

# Menghitung dan menampilkan keliling lingkaran
hasil_keliling = lingkaran.keliling(jari_jari)
print(f"Hasil dari keliling lingkaran adalah: {hasil_keliling}")

# Menghitung dan menampilkan luas lingkaran
hasil_luas = lingkaran.luas(jari_jari)
print(f"Hasil luas lingkaran adalah: {hasil_luas}")
