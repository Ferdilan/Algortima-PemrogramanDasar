# Inisialisasi array dua dimensi
Array = [[0 for j in range(5)] for i in range(4)]

# Input elemen array menggunakan perulangan
for i in range(4):
    for j in range(5):
        Array[i][j] = int(input(f"Masukkan elemen Array1[{i}][{j}]: "))

# Tampilkan isi array
print("Isi Array1:")
for i in range(4):
    for j in range(5):
        print(Array[i][j], end=" ")
    print()

# Hitung jumlah total isi array
total = sum(sum(row) for row in Array)

# menampilkan jumlah total
print(f"Jumlah total isi Array: ", total)
