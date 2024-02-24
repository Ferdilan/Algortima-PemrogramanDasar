
N = int(input("Masukkan nilai N: "))

for i in range(N):
    # Cetak pola dari 1 hingga N atau dari N ke 1 bergantian
    for j in range(1, N + 1):
        print(j, end='')
    print()
    
    for j in range(N, 0, -1):
        print(j, end='')
    print()
