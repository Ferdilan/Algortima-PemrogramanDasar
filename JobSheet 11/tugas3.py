def cek_prima_rekursif(n, i=2):
    # Jika bilangan kurang dari 2, maka bukan prima
    if n < 2:
        return False
    # Jika bilangan sama dengan 2, maka prima
    elif n == 2:
        return True
    # Jika n habis dibagi i, maka bukan prima
    elif n % i == 0:
        return False
    # Jika kuadrat i lebih besar dari n, maka prima
    elif i * i > n:
        return True
    # Rekursif, panggil fungsi dengan i yang ditambah 1
    else:
        return cek_prima_rekursif(n, i + 1)

bilangan = int(input("Masukkan bilangan: "))

# Memanggil fungsi cek_prima_rekursif
hasil = cek_prima_rekursif(bilangan)

if hasil:
    print(f"{bilangan} adalah bilangan prima.")
else:
    print(f"{bilangan} bukan bilangan prima.")
    

