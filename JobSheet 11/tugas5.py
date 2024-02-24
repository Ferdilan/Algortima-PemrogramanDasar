def jumlah_pasangan_kelinci(bulan):
    # Base case: Jika bulan kurang dari atau sama dengan 2, maka mengembalikan return 1 (pasangan awal)
    if bulan <= 2:
        return 1
    # Jumlah pasangan pada bulan sekarang adalah jumlah pasangan pada bulan sebelumnya dikalikan 2
    else:
        return jumlah_pasangan_kelinci(bulan - 2) * 2

# bulan ke 12
bulan_ke = 12

# Memanggil fungsi jumlah_pasangan_kelinci
hasil = jumlah_pasangan_kelinci(bulan_ke)

# Menampilkan hasil
print(f"Setelah {bulan_ke} bulan, terdapat {hasil} pasangan kelinci.")
