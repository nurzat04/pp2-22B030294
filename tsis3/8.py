def spy_game(l):
    for i in range(len(l)-1):
        if l[i] == 0:
            if l[i+1] == 0:
                if l[i+2] == 7:
                    return True
    return False

n = input()
l = n.split()

for i in range(len(l)):
    l[i]= int(l[i])

print(spy_game(l))
