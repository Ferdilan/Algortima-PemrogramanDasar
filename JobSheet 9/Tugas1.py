matriks = []
for i in range(3):
    row = []
    for j in range(4):
        row.append(0)
    matriks.append(row)
    
for i in range (3):
    for j in range (4):
        matriks[i][j] = int(input(f"Masukkan nilai untuk matriks [{i}][{j}]: "))

print("Isi Matriks: ")
for i in range(3):
    for j in range(4):
        print(matriks[i][j], end=" ")
    print()
    
max_elemen = max(max(row) for row in matriks)

print("Nilai terbesar dari elemen adalah:", max_elemen)
