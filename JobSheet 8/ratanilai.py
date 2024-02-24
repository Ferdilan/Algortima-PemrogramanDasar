jml_mahasiswa = int(input("Masukkan jumlah Mahasiswa: "))
nilai_mahasiswa = []

for i in range(jml_mahasiswa):
    input_nilai = float(input("Masukkan nilai mahasiswa ke-%d: " % (i + 1)))
    nilai_mahasiswa.append(input_nilai)
    
total_nilai = sum(nilai_mahasiswa)
rata_rata_nilai = total_nilai / len(nilai_mahasiswa)
print("Rata rata nilai mahasiswa: %.2f" % rata_rata_nilai)

#Modifikasi untuk pertanyaan nomor 2
nilai_lulus = [nilai for nilai in nilai_mahasiswa if nilai >= 70]
if len(nilai_lulus) > 0:
    rata_rata_lulus = sum(nilai_lulus) / len(nilai_lulus)
    print("Rata rata nilai mahasiswa yang lulus: %.2f" % rata_rata_lulus)
else:
    print("Tidak ada mahasiswa yang lulus.")
