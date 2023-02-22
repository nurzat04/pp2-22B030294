def downgen(n):
    for x in reversed(range(n)):
        yield x
        
for x in downgen(10):
    print(x)
