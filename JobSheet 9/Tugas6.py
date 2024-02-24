# char KODE [10]
KODE = ["AE", "AG", "AA", "N", "L", "AD", "F", "B", "BE", "DK"]

# char KOTA [10] [12]
KOTA = [
    ["Madiun"],
    ["Kediri"],
    ["Kedu"],
    ["Malang"],
    ["Surabaya"],
    ["Solo"],
    ["Bogor"],
    ["Jakarta"],
    ["Lampung"],
    ["Bali"]
]

# Menampilkan isi array KOTA
for i in range(len(KOTA)):
    print(f"{KODE[i]}: {', '.join(KOTA[i])}")
