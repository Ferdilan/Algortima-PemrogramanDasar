class NumberUtil:
    @staticmethod
    def Max3(bil1, bil2, bil3):
        return max(bil1, bil2, bil3)

    @staticmethod
    def Min3(bil1, bil2, bil3):
        return min(bil1, bil2, bil3)


# Input dari user untuk tiga bilangan
bilangan1 = int(input("Masukkan bilangan 1: "))  
bilangan2 = int(input("Masukkan bilangan 2: "))
bilangan3 = int(input("Masukkan bilangan 3: "))

# Menggunakan kelas NumberUtil untuk mencari nilai maksimum dan minimum
max_value = NumberUtil.Max3(bilangan1, bilangan2, bilangan3)
print(f"Nilai maksimum dari {bilangan1}, {bilangan2}, dan {bilangan3} adalah: {max_value}")

min_value = NumberUtil.Min3(bilangan1, bilangan2, bilangan3)
print(f"Nilai minimum dari {bilangan1}, {bilangan2}, dan {bilangan3} adalah: {min_value}")
