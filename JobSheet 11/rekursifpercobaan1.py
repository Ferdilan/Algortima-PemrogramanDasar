# Fungsi rekursif untuk menghitung faktorial 
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

# fungsi iteratif untuk menghitung faktorial
def faktorial_iteratif(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

# bilangan yg akan dihitung faktorialnya
angka = 5

# menggunakan fungsi rekursif untuk menghitung faktorial
hasil_faktorial = faktorial(angka)
# menggunakan fungsi iteratif untuk menghitung faktorial
hasil_faktorial_iteratif = faktorial_iteratif(angka)

# mencetak hasil faktorial dengan kedua metode
print(f"Hasil Faktorial dari {angka} adalah: {hasil_faktorial}")
print(f"Hasil Faktorial dari {angka} adalah: {hasil_faktorial_iteratif}")
