def has_33(alist):
    for i in range(len(alist)-1):
        if alist[i] == 3:
            if alist[i] == alist[i+1]:
                return True
    return False

n = input()
alist = n.split()

for i in range(len(alist)):
    alist[i] = int(alist[i])

print(has_33(alist))
