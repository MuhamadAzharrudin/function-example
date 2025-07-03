'''
Bangun ruang berbentuk bola dengan jari-jari r, diketahui memiliki volume 4/3 * phi * r**3 
dan luas sebesar 4 * phi * r**2. buatlah sebuah program yang menerima input jari-jari sebuah 
bola dan mencetak volume dan luasnya
pada layar. gunakan phi = 3.14
'''

def vol_bola(r):
    vol = 4/3 * 3.14 * r**3
    return vol

print(vol_bola(7))