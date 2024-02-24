def gambar_pohon_tinggi(tingkat, tinggi_pohon):
    bintang = '*' * (tingkat * 2 - 1)
    spasi = ' ' * (tinggi_pohon - tingkat)
    return spasi + bintang

def gambar_pohon(n):
    tinggi_pohon = n * 2
    tinggi_puncak = n + 1

    for _ in range(n):
        for _ in range(tinggi_puncak):
            print(gambar_pohon_tinggi(_, tinggi_pohon))

def main():
    try:
        n = int(input("Masukkan nilai n: "))
        if n <= 0:
            print("Masukkan nilai yang lebih besar dari 0.")
        else:
            gambar_pohon(n)
    except ValueError:
        print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()



# 1. **`gambar_pohon_tinggi(tingkat, tinggi_pohon):`**
#    - Fungsi ini menghasilkan string untuk setiap tingkat pohon cemara.
#    - Menggunakan variabel `bintang` untuk menyusun simbol "*" berdasarkan tingkat.
#    - Menggunakan variabel `spasi` untuk menambahkan spasi di awal setiap baris berdasarkan tinggi pohon dan tingkat.
#    - Mengembalikan string yang telah dibuat.

# 2. **`gambar_pohon(n):`**
#    - Fungsi ini menghasilkan pohon cemara dengan tinggi n.
#    - Menggunakan dua loop, satu untuk setiap baris tinggi pohon (`tinggi_pohon`) dan satu lagi untuk tinggi puncak (`tinggi_puncak`).
#    - Memanggil `gambar_pohon_tinggi` untuk setiap tingkat dan mencetaknya.

# 3. **`main():`**
#    - Fungsi utama berinteraksi dengan pengguna, meminta nilai n, dan kemudian memanggil `gambar_pohon` jika nilai n valid (lebih besar dari 0).
#    - Menggunakan blok try-except untuk menangani kesalahan jika pengguna memasukkan input yang tidak valid.

# 4. **__main__ block:**
#    - Memastikan bahwa program dijalankan hanya jika berada di dalam modul utama (bukan diimpor sebagai modul oleh modul lain). Ketika program dijalankan, fungsi utama (`main()`) dipanggil untuk memulai eksekusi program.