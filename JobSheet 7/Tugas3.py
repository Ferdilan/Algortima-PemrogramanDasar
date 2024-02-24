N = int(input("Masukkan N: "))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == 1 or i == N or j == 1 or j == N:
            print(N, end=" ")
        else:
            print(" ", end=" ")
    print()
