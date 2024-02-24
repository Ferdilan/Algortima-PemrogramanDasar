# matriks = [
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# for i in range (2):
#     for j in range (3):
#         matriks[i][j] = int(input(f"Masukkan nilai untuk matriks [{i}][{j}]: "))
        
# print("Isi Matriks: ")
# for i in range(2):
#     for j in range(3):
#         print(matriks[i][j], end=" ")
#     print()
        
        
# Langkah ke 7 melakukan perulangan menggunakan while
matriks = [
    [0, 0, 0],
    [0, 0, 0]
]

i = 0
while i < 2:
    j = 0
    while j < 3:
        matriks[i][j] = int(input(f"Masukkan nilai untuk matriks [{i}][{j}]: "))
        j += 1
    i += 1

print("Isi Matriks: ")
i = 0
while i < 2:
    j = 0
    while j < 3:
        print(matriks[i][j], end=" ")
        j += 1
    print()
    i += 1
