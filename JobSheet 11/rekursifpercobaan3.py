# fungsi rekursif untuk menghitung saldo akhir
def hitungBunga(saldo, tahun):
    if tahun == 0:
        return saldo
    else:
        return 1.11* hitungBunga(saldo, tahun - 1)
# input saldo dan tahun
saldo_awal = float(input("Masukkan saldo awal: "))
jumlah_tahun = int(input("Masukkan jumlah tahun: "))

# memanggil fungsi rekursif
hasil_akhir = hitungBunga(saldo_awal, jumlah_tahun)
# menampilkan fungsi rekursif
print(f"Hasil setelah {jumlah_tahun} tahun adalah {hasil_akhir} ")
