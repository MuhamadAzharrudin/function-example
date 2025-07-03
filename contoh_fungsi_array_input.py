nilai_uts = [60, 50, 34, 88, 92, 64, 57, 83]
nilai_uas = [80, 70, 94, 88, 92, 64, 87, 83]

def cari_rata_rata(list_nilai):
    jumlah_nilai = 0
    banyak_nilai = 0
    for nilai in list_nilai:
        jumlah_nilai += nilai
        banyak_nilai += 1
    rata_rata = jumlah_nilai / banyak_nilai
    return rata_rata

print(cari_rata_rata(nilai_uts))
print(cari_rata_rata(nilai_uas))