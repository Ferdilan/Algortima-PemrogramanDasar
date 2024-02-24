# # Tanpa class
# panjang = int(input("Masukkan panjang persegi panjang: "))
# lebar = int(input("Masukkan lebar persegi panjang: "))
    
# luas_persegi_panjang = panjang * lebar 
# print("Luas persegi panjang adalah: ", luas_persegi_panjang)

# panjang_balok = int(input("Masukkan panjang balok: "))
# lebar_balok = int(input("Masukkan lebar balok: "))
# tinggi_balok = int(input("Masukkan tinggi balok: "))

# volume_balok = panjang_balok*lebar_balok*tinggi_balok
# print("Volume balok adalah: ", volume_balok)


# Dengan class
class Prak6:
    @staticmethod
    def luas_persegi_panjang(panjang, lebar):
        return panjang*lebar
    @staticmethod
    def volume_balok(panjang, lebar, tinggi):
        return panjang*lebar*tinggi

panjang_persegi = int(input("Masukkan panjang persegi panjang: "))
lebar_persegi = int(input("Masukkan lebar persegi panjang: "))

luas_persegi = Prak6.luas_persegi_panjang(panjang_persegi, lebar_persegi)
print("Luas persegi panjang: ", luas_persegi)

panjang_balok = int(input("Masukkan panjang balok: "))
lebar_balok = int(input("Masukkan lebar balok: "))
tinggi_balok = int(input("Masukkan tinggi balok:" ))

vol_balok = Prak6.volume_balok(panjang_balok, lebar_balok, tinggi_balok)
print("Volume balok adalah: ", vol_balok)
                         