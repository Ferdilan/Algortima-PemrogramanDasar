# Import fungsi isi_array_ujian dari Tugas4
from Tugas4 import isi_array_ujian

# Fungsi untuk menemukan nilai terbesar dan terkecil dalam array
def nilai_terbesar_terkecil(arr):
    nilai_terbesar = max(arr)
    nilai_terkecil = min(arr)
    
    return nilai_terbesar, nilai_terkecil
    
# Fungsi utama
def main():
    # Inisialisasi array nilai ujian
    array_ujian = []

    # Jumlah mahasiswa yang diinginkan
    jumlah_mahasiswa = 10
    
    # Mengisi array nilai ujian dengan fungsi dari modul eksternal
    isi_array_ujian(array_ujian, jumlah_mahasiswa)
         
    # Menghitung total nilai dan rata-rata nilai mahasiswa
    total_nilai = sum(array_ujian)
    rata_rata_nilai = total_nilai / jumlah_mahasiswa
    
    # Mendapatkan nilai terbesar dan terkecil
    terbesar, terkecil = nilai_terbesar_terkecil(array_ujian)
    
    # Menampilkan hasil
    print(f"Nilai rata-rata mahasiswa: {rata_rata_nilai}")
    print(f"Nilai Terbesar Mahasiswa: {terbesar}")
    print(f"Nilai Terkecil Mahasiswa: {terkecil}")

# Memanggil fungsi main jika program dieksekusi langsung
if __name__ == "__main__":
    main()
