def palin(n):
    if n == n[::-1]:
        return True
    else:
        return False

n = input()
print(palin(n))