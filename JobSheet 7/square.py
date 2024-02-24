# N = int(input("Masukkan nilai N: "))

# iouter = 1
# for iouter in range(iouter, N+1):
#     i=1
#     for i in range(i, N+1):
#         print('*', end='')
#     print()


#Modifikasi program untuk pertanyaan nomor 4
N = int(input("Masukkan nilai N: "))

for iouter in range(1, N+1):
    for i in range(1, iouter + 1):
        print('*', end='')
    print()
