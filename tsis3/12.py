def histogram(l):
    for i in range(len(l)):
        print("*" * l[i])

n = input()
l = n.split()

for i in range(len(l)):
    l[i] = int(l[i])

histogram(l)