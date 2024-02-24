# kolom = int(input("Masukkan jumlah kolom: "))
# baris =  int(input("Masukkan jumlah baris: "))

# matriks = []
# for i in range(baris):
#     row = []
#     for j in range(kolom):
#         row.append(0)
#     matriks.append(row)
    
# for i in range (baris):
#     for j in range (kolom):
#         matriks[i][j] = int(input(f"Masukkan nilai untuk matriks [{i}][{j}]: "))
        
# print("Isi Matriks: ")
# for i in range(baris):
#     for j in range(kolom):
#         print(matriks[i][j], end=" ")
#     print()
    

#  menggunakan perulangan while
kolom = int(input("Masukkan jumlah kolom: "))
baris =  int(input("Masukkan jumlah baris: "))

matriks = []
i = 0

while i < baris:
    row = []
    j = 0
    while j < kolom:
        row.append(0)
        j += 1
    matriks.append(row)
    i += 1

i = 0
while i < baris:
    j = 0
    while j < kolom:
        matriks[i][j] = int(input(f"Masukkan nilai untuk matriks [{i}][{j}]: "))
        j += 1
    i += 1

print("Isi Matriks: ")
i = 0
while i < baris:
    j = 0
    while j < kolom:
        print(matriks[i][j], end=" ")
        j += 1
    print()
    i += 1
