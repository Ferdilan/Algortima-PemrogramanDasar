kolom = int(input("Masukkan jumlah kolom: "))
baris =  int(input("Masukkan jumlah baris: "))

array = []
for i in range(baris):
    row = []
    for j in range(kolom):
        row.append(0)
        array.append(row)

def nilai_min(array):
    # Temukan nilai minimum
    min_value = min(min(row) for row in array)
    return min_value

def nilai_min_jumlah(array):
    # Temukan nilai minimum dan jumlahnya
    min_value = min(min(row) for row in array)
    count_min_value = sum(row.count(min_value) for row in array)
    locations = [(i, j) for i, row in enumerate(array) for j, 
                val in enumerate(row) if val == min_value]
    return min_value, count_min_value, locations

def kondisi_array(array):
    # Periksa apakah ada nilai 50 di dalam array
    ada_nilai_50 = any(50 in row for row in array)
    return "ADA" if ada_nilai_50 else "TIDAK ADA"

# Inisialisasi array dua dimensi
baris = 3
kolom = 4
Array3 = [[0 for j in range(kolom)] for i in range(baris)]

# Input elemen array menggunakan perulangan
for i in range(baris):
    for j in range(kolom):
        Array3[i][j] = int(input(f"Masukkan elemen Array3[{i}][{j}]: "))

# Tampilkan isi array
print("Isi Array3:")
for i in range(baris):
    for j in range(kolom):
        print(Array3[i][j], end=" ")
    print()

# Pilihan menu
while True:
    print("\nPilihan Menu (1/2/3/4):")
    print("1. (Nilai MIN)")
    print("2. (Nilai MIN & Jumlahnya)")
    print("3. (Kondisi Array)")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1-4): ")

    if pilihan == "1":
        print("Nilai MIN: ", nilai_min(Array3))
    elif pilihan == "2":
        min_val, count_min_val, locations = nilai_min_jumlah(Array3)
        print(f"Nilai MIN: {min_val}, Jumlahnya: {count_min_val}, Lokasi: {locations}")
    elif pilihan == "3":
        print("Kondisi Array:", kondisi_array(Array3))
    elif pilihan == "4":
        print("Terima kasih.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1-4.")
