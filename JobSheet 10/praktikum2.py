class Berisalam:
    def sapa (self, pesan="Halo selamat pagi!"):
        print (pesan)
    
class Beriucapan:
    def beri_ucapan(self, ucapan):
        print(ucapan)
        
objek_salam = Berisalam()
objek_salam.sapa()

objek_ucapan = Beriucapan()
salam = "selamat Datang di Kelas TT-1B"
objek_ucapan.beri_ucapan(salam)
