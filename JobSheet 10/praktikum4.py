class Opertator:
    def kali(self, angka1, angka2):
        hasil = angka1 * angka2
        return(hasil)
    def kurang(self, angka1, angka2):
        hasil = angka1 - angka2
        return(hasil)
    
operator = Opertator()
angka1 = int(input("Masukkan angka 1: "))
angka2 = int(input("Masukkan angka 2: "))

hasil_kali = operator.kali(angka1, angka2)
print(f"Hasil dari perkalian adalah: {hasil_kali}")

hasil_kurang = operator.kurang(angka1, angka2)
print(f"Hasil dari pengurangan adalah: {hasil_kurang}") 