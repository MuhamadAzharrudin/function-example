'''
Jika :

faktorial 0 = 1
faktorial 1 = 1
faktorial 2 = 2 x 1
faktorial 3 = 3 x 2 x 1
faktorial 4 = 4 x 3 x 2 x 1
faktorial 5 = 5 x 4 x 3 x 2 x 1
faktorial n = n x faktorial(n-1)
Buatlah sebuah fungsi rekursif yang menghitung faktorial sebuah bilangan positif n
'''

def bil_faktorial (n):
    if n == 0:
        return 1
    else:
        faktorial = n * bil_faktorial (n-1)
        return faktorial
    
for i in range(5+1):
    print(bil_faktorial(i), end=" ")
