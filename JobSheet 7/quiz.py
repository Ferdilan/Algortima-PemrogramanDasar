import random

menu = 'y'

while menu.lower() == 'y':
    number = random.randint(1, 10)
    success = False
    while not success:
        try:
            answer = int(input("Tebak angka (1-10): "))
            if answer < number:
                print("Angka tebakan terlalu kecil. Coba lagi!")
            elif answer > number:
                print("Angka tebakan terlalu besar. COba lagi!")
            else:
                success = True
        except ValueError:
            print("Masukkan angka yang valid (1-10)!: ")
    print("Selamat! Anda menebak dengan benar.")
    menu = input("Apakah Anda ingin mengulang perminan (Y/y), jika tidak tekan Enter? ")
    
print("Terima kasih telah bermain!")