def tampilderet(x):
    if x > 0:
        print(x, end='')
        tampilderet(x - 1)
    else:
        print()

# COntoh pemanggilan fungsi
angka = 5
tampilderet(angka)

# artikel tentang rekursif
# https://jagongoding.com/python/dasar/fungsi-rekursif/