def gensquares(a, b):
    for i in range(a, b):
        yield i ** 2
a1 = int(input())
b1 = int(input())
for x in gensquares(a1, b1):
    print(x)