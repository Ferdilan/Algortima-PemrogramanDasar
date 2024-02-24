def bil_prima(angka):
    # Fungsi untuk memeriksa apakah suatu bilangan adalah bilangan prima atau bukan
    if angka < 2:
        return False
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            return False
    return True

def hasilkan_prima(jumlah):
    # Fungsi untuk menghasilkan jumlah bilangan prima pertama
    prima = []
    angka = 2
    while len(prima) < jumlah:
        if bil_prima(angka):
            prima.append(angka)
        angka += 1
    return prima

def utama():
    try:
        jumlah = int(input("Masukkan nilai N: "))
        if jumlah <= 0:
            print("Silakan masukkan nilai N yang lebih besar dari 0.")
        else:
            bilangan_prima = hasilkan_prima(jumlah)
            print(f"{jumlah} bilangan prima: {bilangan_prima}")
    except ValueError:
        print("Masukkan angka yang valid.")

if __name__ == "__main__":
    utama()



# 1. **bil_prima(angka):**
#    - Fungsi ini memeriksa apakah suatu angka adalah bilangan prima atau bukan.
#    - Jika angka kurang dari 2, fungsi mengembalikan False karena bilangan prima harus lebih besar dari 1.
#    - Fungsi kemudian melakukan iterasi dari 2 hingga akar kuadrat dari angka (inklusif). Jika angka dapat dibagi habis oleh suatu bilangan selain 1 dan dirinya sendiri, maka bukan bilangan prima, dan fungsi mengembalikan False. Jika tidak ada bilangan yang membagi habis, angka adalah bilangan prima, dan fungsi mengembalikan True.

# 2. **hasilkan_prima(jumlah):**
#    - Fungsi ini menghasilkan jumlah bilangan prima pertama.
#    - Menggunakan loop while, fungsi ini terus mencari bilangan prima hingga jumlah bilangan prima yang sudah dihasilkan mencapai jumlah yang diinginkan.
#    - Untuk setiap angka, fungsi memanggil `bil_prima` untuk memeriksa apakah angka tersebut adalah bilangan prima. Jika iya, angka tersebut ditambahkan ke dalam daftar `prima`.

# 3. **utama():**
#    - Fungsi utama berinteraksi dengan pengguna untuk meminta input jumlah bilangan prima yang ingin dihasilkan (n).
#    - Menggunakan blok try-except untuk menangani kesalahan jika pengguna memasukkan input yang tidak valid (misalnya, bukan angka).
#    - Jika nilai n kurang dari atau sama dengan 0, program memberi pesan kesalahan. Jika tidak, program memanggil `hasilkan_prima` untuk menghasilkan bilangan prima dan mencetaknya.

# 4. **__main__ block:**
#    - Memastikan bahwa program dijalankan hanya jika berada di dalam modul utama (bukan diimpor sebagai modul oleh modul lain). Ketika program dijalankan, fungsi utama (`utama()`) dipanggil untuk memulai eksekusi program.