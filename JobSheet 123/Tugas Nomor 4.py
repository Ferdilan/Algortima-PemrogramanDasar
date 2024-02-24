
suhu = float(input("Masukkan Suhu   :"))

celcius = suhu
strcelcius = str(celcius)
reamur = 4/5*suhu
strreamur = str(reamur)
fahrenheit = 9/5*celcius+32
strfahrenheit = str(fahrenheit)
kelvin = celcius + 372
strkelvin = str(kelvin)

print("Suhu "+strcelcius+" derajat celcius")
print("Suhu "+strreamur+" derajat reamur")
print("Suhu "+strfahrenheit+" derajat fahrenheit")
print("Suhu "+strkelvin+" derajat kelvin")
