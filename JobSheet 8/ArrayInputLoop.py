nilai_uas = [] *6

for i in range(6):
    input_nilai_uas = float(input("Masukkan nilai UAS ke-%d: " % (i + 1) ))
    nilai_uas.append(input_nilai_uas)

print("Nilai UAS yang dimasukkan: ")
for indeks, nilai in enumerate(nilai_uas, start=1):
    print("UAS ke-%d: %.2f" % (indeks, nilai))



# Pertanyaan nomor 3
print("Status Lulus atau Tidak Lulus: ")
for i, nilai in enumerate(nilai_uas, start=1):
    status = "Lulus" if nilai >= 70 else "Tidak Lulus"
    print("UAS ke-%d: %s" % (i, status))



# mengubah statemen pada nomor 5
# untuk pertanyaan nomor 2
# print("Nilai yang Lulus: ")
# for i, nilai in enumerate(nilai_uas, start=1):
#     if nilai >= 70:
#         status = "Lulus"
#         print("UAS ke-%d: %s" % (i, status))
