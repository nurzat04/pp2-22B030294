def reverse(n):
    list = n.split()
    list.reverse()
    return ' '.join(list)

n = str(input())
print(reverse(n))