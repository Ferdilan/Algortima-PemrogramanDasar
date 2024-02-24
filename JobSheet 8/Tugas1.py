nilai_array = [] * 5

for i in range(5):
    inputarray = int(input("Masukkan Array: "))
    nilai_array.append(inputarray)

print("Array yang anda masukkan: ")
for i in range(len(nilai_array) - 1, -1, -1):
    print(nilai_array[i])
    