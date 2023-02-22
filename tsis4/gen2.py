def geneven(n):
    for i in range(n):
        if (i % 2) == 0:
            yield i

a = int(input())
for x in geneven(a):
    print(x, end = ",")
