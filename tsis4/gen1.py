def gen(n):
    for i in range(n):
        yield i * i
for x in gen(10):
    print(x)

