def hitung_ip_semester(matakuliah):
    total_sks = 0
    total_bobot = 0

    for mk in matakuliah:
        sks = mk['sks']
        bobot = mk['bobot']
        nilai = mk['nilai']

        total_sks += sks
        total_bobot += sks * bobot

    if total_sks == 0:
        return 0.0  # Menghindari pembagian dengan nol
    else:
        ip_semester = total_bobot / total_sks
        return ip_semester

def main():
    jml_matakuliah = int(input("Masukkan jumlah matakuliah yang diambil: "))

    matakuliah = []
    for i in range(jml_matakuliah):
        nama_mk = input(f"Masukkan nama matakuliah ke-{i + 1}: ")
        sks = int(input(f"Masukkan bobot SKS untuk {nama_mk}: "))
        bobot = float(input(f"Masukkan bobot nilai untuk {nama_mk}: "))
        nilai = float(input(f"Masukkan nilai untuk {nama_mk}: "))

        matakuliah.append({'nama': nama_mk, 'sks': sks, 'bobot': bobot, 'nilai': nilai})

    ip_semester = hitung_ip_semester(matakuliah)

    print("\nDaftar Matakuliah dan Nilai:")
    for mk in matakuliah:
        print(f"{mk['nama']} (SKS: {mk['sks']}, Bobot: {mk['bobot']}, Nilai: {mk['nilai']})")

    print("\nIndeks Prestasi Semester (IPS):", ip_semester)

if __name__ == "__main__":
    main()
