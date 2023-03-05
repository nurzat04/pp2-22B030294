def multiply(n):
    p = 1
    for i in n:
        p *= i
    return p
alist=list(map(int,input().split()))
print(multiply(alist))