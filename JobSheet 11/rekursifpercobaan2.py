# fungsi rekursif untuk menghitung pangkat
def hitungpangkat(x,y):
    if y == 0:
        return 1
    else:
        return x * hitungpangkat(x, y - 1)
    
# input bilangan dan pangkat dari pengguna
bilangan = int(input("Masukkan bilangan: "))
pangkat = int(input("masukkan pangkat: "))

# memanggil fungsi rekursif untuk menghitung pangkat
hasil_pangkat = hitungpangkat(bilangan, pangkat)

# menampilkan hasil pangkat
print(f"Hasil dari bilangan {bilangan} pangkat {pangkat} adalah {hasil_pangkat}")
