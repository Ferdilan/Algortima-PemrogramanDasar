# Inisialisasi array dua dimensi (3x5)
baris = 3
kolom = 5
Array = [[0 for j in range(kolom)] for i in range(baris)]

# Input elemen array menggunakan perulangan
for i in range(baris):
    for j in range(kolom):
        Array[i][j] = int(input(f"Masukkan elemen Array[{i}][{j}]: "))

# Tampilkan isi array
print("Isi Array:")
for i in range(baris):
    for j in range(kolom):
        print(Array[i][j], end=" ")
    print()

# Cetak nilai terbesar dari semua baris
max_per_row = [max(row) for row in Array]
max_overall_row = max(max_per_row)
print(f"\nNilai Terbesar dari Semua Baris: {max_overall_row}")

# Cetak nilai terbesar dari semua kolom
max_per_col = [max(col) for col in zip(*Array)]
max_overall_col = max(max_per_col)
print(f"Nilai Terbesar dari Semua Kolom: {max_overall_col}")
