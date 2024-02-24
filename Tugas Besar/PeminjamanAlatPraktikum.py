#==================================
# Ferdilan
#==================================
# import modul PrettyTabel untuk membuat tabel
# install terlebih dahulu di terminal dengan kode "pip install PrettyTable"
from prettytable import PrettyTable

class AlatTelekomunikasi:
    def __init__(self, nama_alat, jumlah_stok):
        # inisialisasi atribut objek telekomunikasi
        self.nama_alat = nama_alat
        self.jumlah_stok = jumlah_stok
        self.dipinjam = 0
        self.nama_peminjam = None #menggunakan list untuk menyimpan nama
        self.nim_peminjam = None #menggunakan list untuk menyimpan nim

    def pinjam(self, jumlah, nama_peminjam, nim_peminjam):
        # metode untuk meminjam alat
        if self.jumlah_stok - self.dipinjam >= jumlah: #jika jumlah stok dikurangi jumlah yg sudah dipinjam lebih dari atau samadengan jumlah yg diminta maka stok alat masih mencukupi
            self.dipinjam += jumlah #menambahkan jumlah yg dipinjam ke atribut dipinjam
            self.nama_peminjam = nama_peminjam #Menambahkan nim ke list
            self.nim_peminjam = nim_peminjam #Menambahkan nama ke list
            return True #kembalikan nilai true jika peminjaman berhasil
        else: #jika stok alat tidak mencukupi
            print(f"Maaf, stok {self.nama_alat} tidak mencukupi untuk dipinjam.")
            return False
        
    def kembalikan(self, jumlah):
        # metode untuk mengembalikan alat
        print(f"Jumlah dipinjam: {self.dipinjam}, Jumlah yang dikembalikan: {jumlah}")
        if self.dipinjam >= jumlah: #jika jumlah yang dikembalikan sama dengan jumlah dipinjam
            self.dipinjam -= jumlah #maka jumlah yang di pinjam dikurangi dengan jumlah yang di kembalikan 
            nama_peminjam = self.nama_peminjam  #Menyimpan nama peminjam ke variabel sementara sebelum direset ke None
            nim_peminjam = self.nim_peminjam  #Menyimpan nim peminjam ke variabel sementara sebelum direset ke None
            self.nama_peminjam = None
            self.nim_peminjam = None
            return (nama_peminjam, nim_peminjam) #kembalikan data peminjam
        else: #jika jumlah yg dikembalika tidak sesuai
            print(f"Pengembalian gagal, jumlah tidak sesuai.")
            return False
        
    def lihat_peminjam(self):
        # metode menampilkan informasi peminjam
        print(f"Nama peminjam: {self.nama_peminjam}")
        print(f"Nim Peminjam: {self.nim_peminjam}")
        print(f"Alat: {self.nama_alat}")
        print(f"Jumlah dipinjam: {self.dipinjam}")
        print("=============================")
#==================================
# Ferdilan
#==================================
        
#==================================
# Wizza
#==================================
class BengkelTelekomunikasi:
    def __init__(self):
        # inisialisasi list kosong untuk menyimpan alat alat yang ada di bengekl
        self.alat = []

    def tambah_alat(self, nama_alat, jumlah_stok):
        # metode untuk menambahkan alat baru ke bengkel
        alat_baru = AlatTelekomunikasi(nama_alat, jumlah_stok)#membuat objek baru dari kelas AlatTelekomunikasi dengan nama dan jumlah stok sebagai parameter
        self.alat.append(alat_baru) #menambahkan objek_alat baru ke dalam list alat yg merupakan atribut dari objek bengkeltelekomunikasi
        print(f"Alat {nama_alat} dengan stok {jumlah_stok} berhasil ditambahkan.")
        self.lihat_stok() #memanggil fungsi lihat_stok yg kemudian ditampilkn setelah penambahan alat baru
        
    def pinjam_alat(self, nama_alat, jumlah, nama_peminjam, nim_peminjam):    
        # metode untuk meminjam alat dari bengkel
        for alat in self.alat: #melakuka iterasi pada setiap alat yang ada dibengkel
              if alat.nama_alat == nama_alat: #memeriksa apakah nama alat pada iterasi cocok dengan nama alat yg ingin dipinjam
                  if alat.pinjam(jumlah, nama_peminjam, nim_peminjam): #memanggil metode pinjam dari objek alattelekomunikasi dengan memberikan jumlah, nama peminjam, dan NIM peminjam sebagai argumen.
                      print("==========Data Peminjam==========")
                      print(f"Nama Peminjam       : {nama_peminjam}")
                      print(f"Nim Peminjam        : {nim_peminjam}")
                      print(f"Alat yang dipinjam  : {nama_alat}")
                      print(f"Jumlah dipinjam     : {jumlah}")
                      return True #mengembalikan nilai true jika peminjaman berhasil dan mencetak data peminjam
                  else:#jika peminjaman gagal 
                      print(f"peminjaman alat {nama_alat} oleh {nama_peminjam} gagal")
        print(f"Maaf, {nama_alat} tidak tersedia di bengkel ini") #jika alat tidak ditemukan dalam iterasi 
        return False
#==================================
# Wiza
#==================================

#==================================
# Rahayu
#==================================
    def kembalikan_alat(self, nama_alat, jumlah, nama_peminjam, nim_peminjam):
        # metode untuk mengembalikan alat ke bengkel
        for alat in self.alat: #melakukan iterasi setiap alat yang ada di bengkel
            # Mencocokkan nama peminjam, nim, dan alat yang dipinjam
            if alat.nama_alat == nama_alat and alat.nim_peminjam == nim_peminjam and alat.nama_peminjam.lower() == nama_peminjam.lower():
                berhasil, nama_pengembali = alat.kembalikan(jumlah) #memanggil metode kembalikan dari objek alattelekomunikasi dan menyimpan hasilnya
                if berhasil: #jika berhasil 
                    if nim_peminjam is not None:
                        print(f"Alat {nama_alat} sebanyak {jumlah} telah dikembalikan oleh {nama_peminjam} NIM: {nim_peminjam}")
                    else:
                        print(f"Alat {nama_alat} sebanyak {jumlah} telah dikembalikan oleh {nama_pengembali}")
                    return True
                else: #jika gagal
                    print(f"Pengembalian alat {nama_alat} sebanyak {jumlah} gagal")
                    return False
        # jika alat tidak ditemukan dalam iterasi 
        print(f"Maaf, {nama_alat} tidak tersedia di bengkel ini atau tidak dipinjam oleh {nama_peminjam} {nim_peminjam}")
        return False
    
    def tampilkan_semua_peminjam(self):
        # metode untuk menampilkan semua data peminjam
        data_tabel = [["Nama Peminjam", "nim", "Alat Dipinjam", "Jumlah"]] #membuat header tabel
        
        alat_ditemukan = False
        for alat in self.alat: #melakukan iterasi alat yg ada di bengkel
            if alat.dipinjam > 0: #memeriksa apakah alat sedang dipinjam (jumlah lebih dari nol)
                alat_ditemukan = True #jika alat sedang dipinjam mengubah variabel menjadi TRUUUU
                data_tabel.append([alat.nama_peminjam, alat.nim_peminjam,  alat.nama_alat, alat.dipinjam]) #menambabhkan baris data ke tabel untuk setiap yg sdang dipinjam
                         
        if not alat_ditemukan: #jika tidak ada alat yg sedang dipinjam cetak pesan dibawah
            print("Maaf, tidak alat yang sedang dipinjam di bengkel ini.")
        
        else:
            # membuat dan menampilkan Tabel
            tabel = PrettyTable(data_tabel[0])
            tabel.add_rows(data_tabel[1:])
            print(tabel)   
            
    def lihat_stok(self):
        # metode untuk melihat stok alat yang tersedia di bengkel
        data_tabel = [["Nama Alat", "Jumlah Tersedia"]]
        for alat in self.alat: #iterasi setiap alat yg ada dibengkel
            stok_tersedia = alat.jumlah_stok - alat.dipinjam #menghitung stok tersedia untuk setiap alat. jumlah stok dikurangi jumlah alat yg sedang dipinjam. jumlah stok dan jumlah alat yg dipinjam didpat dri list alat
            data_tabel.append([alat.nama_alat, stok_tersedia]) #menambahkan baris data ke tabel dengan informasi nama alat dan stok tersedia
        if not self.alat: #jika tidak ada alat di bengkel
            print("Maaf, tidak ada alat yang tersedia di bengkel ini.")
        else: #jika ada alat dibengkel 
            # membuat dan menampilkan Tabel
            tabel = PrettyTable(data_tabel[0])
            tabel.add_rows(data_tabel[1:])
            print(tabel)
#==================================
# Rahayu
#==================================


#==================================
# Valent
#==================================
def main():#fungsi untk mengatur menu dan interaksi pengguna
    bengkel = BengkelTelekomunikasi() #membuat objek bengkel dari kelas BengkelTelekomunikasi()

    while True: #looping tidak terbatas agar pengguna dapat memilih beberapa menu tanpa keluar dari program
        print("\n=====Peminjaman Alat Praktikum Bengkel Teknik Telekomunikasi=====")
        print("Silahkan Pilih Menu:")
        print("1. Tambah Alat")
        print("2. Pinjam Alat")
        print("3. Kembalikan Alat")
        print("4. Lihat Peminjam")
        print("5. Stok Alat")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-4): ") # masukkan menu dari 1-4

        if pilihan == "1":
            print("==========Tambah Alat==========")
            nama_alat = input("Masukkan nama alat: ")
            jumlah_stok = int(input("Masukkan jumlah stok: "))
            bengkel.tambah_alat(nama_alat, jumlah_stok) #menambahkan alat baru ke daftar alat yg ada di bengkel
        elif pilihan == "2":
            print("==========Peminjaman Alat==========")
            nama_peminjam = input("Masukkan Nama peminjam: ")
            nim_peminjam = int(input("Masukkan NIM peminjam: "))
            nama_alat = input("Masukkan nama alat yang ingin dipinjam: ")
            jumlah = int(input("Masukkan jumlah alat yang ingin dipinjam: "))
            bengkel.pinjam_alat(nama_alat, jumlah, nama_peminjam, nim_peminjam) #mencari alat yg sesuai nama alat yg akan dipinjam kemudian melakukan penminajamn
        elif pilihan == "3":
            print("==========Pengembalian Alat=========")
            nama_peminjam = input("Masukkan Nama peminjam: ")
            nim_peminjam = int(input("Masukkan NIM peminjam: "))
            nama_alat = input("Masukkan nama alat yang ingin dikembalikan: ")
            jumlah = int(input("Masukkan jumlah alat yang ingin dikembalikan: "))
            print("==========Alat Dikembalikan==========")   
            bengkel.kembalikan_alat(nama_alat, jumlah, nama_peminjam, nim_peminjam) #mencari alat yg sesuai nama alat yg akan dikembalikan kemudian melakukan pengembalian
        elif pilihan == "4":
            print("==========Data Peminjam==========")
            bengkel.tampilkan_semua_peminjam() #panggil method tampilkan_semua_peminjam() dari kelas bengkel telekomunikasi
        elif pilihan == "5":
            print("==========Alat Tersedia==========")
            bengkel.lihat_stok() #panggil method lihat_stok() dari bengkel telekomunikasi
        elif pilihan == "6":
            exit() #keluar dari program
        else:#inputan tidak 1-4
            print("Pilihan tidak valid. Silakan pilih menu 1-4.")

if __name__ == "__main__": #mengecek apakah file ini dijalankan sebagai program utama 
    main() #jika ya panggil fungsi main

#==================================
# Valent
#==================================