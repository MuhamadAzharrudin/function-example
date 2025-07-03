'''
deret_fibonancci = 0 1 1 2 3 5 8 13 21
f(1) = 0
f(2) = 1
f(n) = f(n-1) + f(n-2)
'''

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = fibonacci (n-1) + fibonacci (n-2)
        return fib
    
for i in range (1,11):
    print(fibonacci (i), end=" ")