kolom = int(input("Masukkan jumlah kolom: "))
baris =  int(input("Masukkan jumlah baris: "))

matriks = []
for i in range(baris):
    row = []
    for j in range(kolom):
        row.append(0)
    matriks.append(row)
    
for i in range (baris):
    for j in range (kolom):
        matriks[i][j] = int(input(f"Masukkan nilai untuk matriks [{i}][{j}]: "))
        
print("Matriks Awal: ")
for i in range(baris):
    for j in range(kolom):
        print(matriks[i][j], end=" ")
    print()

transpose = [[matriks[j][i] for j in range(len(matriks))] for i in range(len(matriks[0]))]

print("Matriks Transpose:")
for row in transpose:
    print(row)
