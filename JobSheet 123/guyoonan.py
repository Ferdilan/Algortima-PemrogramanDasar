print("===========Kalkulator Sederhana===========")

while True:
    angka1 = input("Masukkan angka pertama           (atau ketik 'q' untuk keluar): ")

    if angka1.lower() == 'q':
        break

    angka2 = input("Masukkan angka kedua             (atau ketik 'q' untuk keluar): ")

    if angka2.lower() == 'q':
        break

    hasil_gabung = angka1 + angka2

    print("Angka yang anda tambahkan        : " + angka1 + " + " + angka2)
    print("Hasil Penambahan                 :", hasil_gabung)
    print("================Sederhana================")

print("Terima kasih. Program berakhir.")
