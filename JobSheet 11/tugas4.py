def fpb_euclid_rekursif(m, n):
    # Basis: Jika n adalah 0, maka FPB adalah m
    if n == 0:
        return m
    # Rekursif: Panggil fungsi dengan argumen n dan m%n
    else:
        return fpb_euclid_rekursif(n, m % n)

# Contoh penggunaan dengan bilangan 45 dan 20
bilangan_m = int(input("Masukkan bilangan m: "))
bilangan_n = int(input("Masukkan bilangan n: "))

# Memanggil fungsi fpb_euclid_rekursif
hasil_fpb = fpb_euclid_rekursif(bilangan_m, bilangan_n)

# Menampilkan hasil
print(f"FPB dari {bilangan_m} dan {bilangan_n} adalah {hasil_fpb}")

