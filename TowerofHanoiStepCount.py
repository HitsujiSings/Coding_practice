def count(n):
    if n > 0:
        return count(n-1)*2+1
    else:
        return 1
print(count(7))



