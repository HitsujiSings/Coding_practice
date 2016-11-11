def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))

def recursionA(n,x):
    if n>0:
        x= x+n
        return recursionA(n-1,x)
    else:
        return x


print(recursionA(5,0))

