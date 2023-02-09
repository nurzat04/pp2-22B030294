import itertools

def permute(str):
    mylist = [''.join(i) for i in itertools.permutations(str)]
    for i in mylist:
        print(i, end = " ")

n = input()
permute(n)