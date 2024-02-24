jml_array = int(input("Masukkan Jumlah Array: "))
nilai_array = []

for i in range(jml_array):
    input_array = int(input("Masukkan Array ke %d: " % (i + 1)))
    nilai_array.append(input_array)
    max_elemen = max(nilai_array)
print("Elemen terbesar dalam array: ", max_elemen)
