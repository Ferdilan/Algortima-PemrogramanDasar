jml_array = int(input("Masukkan Jumlah Array: "))
nilai_array = []

for i in range(jml_array):
    input_array = int(input("Masukkan Array ke %d: " % (i + 1)))
    nilai_array.append(input_array)
    # Menghapus elemen dengan nilai tertentu dari list
element_dihapus = []
elemen = int(input("Masukkan elemen yang akan dihapus: "))
element_dihapus.append(elemen)
nilai_array.remove(elemen)
print("Elemen yang tersisa", nilai_array)