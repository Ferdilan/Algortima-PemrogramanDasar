jml_array = int(input("Masukkan Jumlah Array: "))
nilai_array = []

for i in range(jml_array):
    input_array = int(input("Masukkan Array ke %d: " % (i + 1)))
    nilai_array.append(input_array)


ganjil = []
genap = []

for bilangan in nilai_array:
    if bilangan % 2 != 0:
        ganjil.append(bilangan)
    else:
        genap.append(bilangan)
        
for bilangan in ganjil:
    print("Bilangan Ganjil: ", bilangan)

for bilangan in genap:
    print("Bilangan Genap: ", bilangan)