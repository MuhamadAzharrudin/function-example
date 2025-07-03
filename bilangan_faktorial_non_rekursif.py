'''
Jika :

faktorial 0 = 1
faktorial 1 = 1
faktorial 2 = 2 x 1
faktorial 3 = 3 x 2 x 1
faktorial 4 = 4 x 3 x 2 x 1
faktorial 5 = 5 x 4 x 3 x 2 x 1
faktorial n = n x faktorial(n-1)
Buatlah fungsi yang menghitung faktorial bilangan bulat n, tanpa menggunakan teknik rekursif
'''

def faktorial(n):
    f = 1
    for i in range (2,n+1):
        f = i * f
    return f
    
for i in range(6):
    print(faktorial(i), end=" ")