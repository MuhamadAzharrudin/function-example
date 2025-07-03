nilai_berhitung = [["Upin",80,90],["Jarjit",70,75],["Ipin",94,90],["Mail",88,96],["Ehsan",92,75]]

#print(nilai_berhitung[3][0])
#print(nilai_berhitung[1][2])

# buat fungsi untuk mencari siswa tadika mesra dengan nilai berhitung paling tinggi
# nilai berhitung dihitung dari rata-rata dua ujian


def cari_tertinggi (list_nilai):
    nilai_tertinggi = 0
    siswa_nilai_tertinggi = ""
    for nilai_siswa in list_nilai:
        siswa = nilai_siswa[0]
        nilai = (nilai_siswa[1] + nilai_siswa[2]) / 2
        if nilai > nilai_tertinggi:
            siswa_nilai_tertinggi = siswa
            nilai_tertinggi = nilai
    return [siswa_nilai_tertinggi, nilai_tertinggi]

print(cari_tertinggi(nilai_berhitung))