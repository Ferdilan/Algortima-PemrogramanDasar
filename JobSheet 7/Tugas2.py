N = int(input("Masukkan N: "))

for i in range(N, 0, -1):
    spaces = " " * (N - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

for i in range(2, N + 1):
    spaces = " " * (N - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
