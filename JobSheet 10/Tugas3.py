def isi_array(arr, n):

    for i in range(n):
        nilai = int(input(f"Masukkan nilai ke-{i+1}: "))
        if i % 2 == 0:  # Hanya mengisi nilai pada indeks ganjil
            arr.append(nilai)
        else:
            arr.append(None)

def main():
    # Mendefinisikan array satu dimensi kosong
    array_satu_dimensi = []

    # Meminta user untuk mengisi array
    panjang_array = int(input("Masukkan panjang array: "))
    isi_array(array_satu_dimensi, panjang_array)

    # Menampilkan isi array setelah diisi
    print("Isi array satu dimensi:")
    for nilai in array_satu_dimensi:
        print(nilai)

# Memanggil fungsi main
if __name__ == "__main__":
    main()
