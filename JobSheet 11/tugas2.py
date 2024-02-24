# Fungsi rekursif untuk penjumlahan
def penjumlahan_rekursif(n):
    # Basis case: jika n = 0, kembalikan 0
    if n == 0:
        return 0
    else: 
        # Langkah rekursif: tambahkan n dengan hasil penjumlahan rekursif dari n-1
        return n + penjumlahan_rekursif(n-1)

# Input nilai n dari pengguna
n = int(input("Masukkan nilai n: "))

# Panggil fungsi rekursif untuk mendapatkan hasil penjumlahan
hasil_penjumlahan = penjumlahan_rekursif(n)

# Tampilkan hasil penjumlahan
print(f"Hasil dari penjumlahan {n} adalah {hasil_penjumlahan}")
