class Persegi:
    def luaspersegi(sisi):
        luas = sisi * sisi
        return luas

sisi_persegi = int(input("Masukkan sisi persegi (integer): "))
hasil = sisi_persegi.luaspersegi(sisi_persegi)
print(f"Luas persegi dengan sisi {sisi_persegi} adalah {hasil}")