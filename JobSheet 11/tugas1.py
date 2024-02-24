# Fungsi rekursif  
def deret_rekursif(n):
    if n >= 0:
        print(n, end=" ")
        deret_rekursif(n-1)

# fungsi iteratif 
def deret_iteratif(n):
    for i in range(n, -1, -1 ):
        print(i, end=" ")

# input angka
angka = int(input("Masukan bilangan n: "))

# Menampilkan deret descending dengan fungsi rekursif
print("Deret Descending Rekursif:")
deret_rekursif(angka)
print()

# Menampilkan deret descending dengan fungsi iteratif
print("Deret Descending Iteratif:")
deret_iteratif(angka)
