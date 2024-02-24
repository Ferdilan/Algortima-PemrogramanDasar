def isi_array_ujian(arr, n):
    # Mengisi array dengan nilai ujian sesuai jumlah mahasiswa
    for i in range(n):
        nilai = int(input(f"Masukkan nilai ujian mahasiswa ke-{i+1}: "))
        arr.append(nilai)
    
def main():
    # Mendefinisikan array satu dimensi kosong
    array_ujian = []

    # Meminta user untuk mengisi array dengan nilai ujian untuk 10 mahasiswa
    jumlah_mahasiswa = 10
    isi_array_ujian(array_ujian, jumlah_mahasiswa)
        
    # Menghitung total nilai dan rata-rata nilai mahasiswa
    total_nilai = sum(array_ujian)
    rata_rata_nilai = total_nilai / jumlah_mahasiswa
    
    # Menampilkan nilai rata-rata mahasiswa
    print(f"Nilai rata-rata mahasiswa: {rata_rata_nilai}")

# Memanggil fungsi main
if __name__ == "__main__":
    main()
