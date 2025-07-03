nilai_berhitung = [["Upin",80,90],["Jarjit",70,75],["Ipin",94,90],["Mail",88,96],["Ehsan",92,75]]

#print(nilai_berhitung[3][0])
#print(nilai_berhitung[1][2])

# buat fungsi untuk mencari siswa tadika mesra dengan nilai berhitung paling tinggi
# nilai berhitung dihitung dari rata-rata dua ujian


def mencari_nilai_tertinggi(nilai_berhitung):
    nilai_tertinggi = 0
    nilai_tertinggi_siswa = ""
    for siswa in nilai_berhitung:
        nilai_rata_rata = (siswa[1] + siswa[2]) / 2
        if nilai_rata_rata > nilai_tertinggi:
            nilai_tertinggi = nilai_rata_rata
            nilai_tertinggi_siswa = siswa [0]
    return nilai_tertinggi_siswa

print(mencari_nilai_tertinggi(nilai_berhitung))

