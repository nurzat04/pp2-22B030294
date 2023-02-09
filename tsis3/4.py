def is_prime(n):
    if n == 0 or n == 1:
        return False

    for j in range(2,n):
        if n%j == 0:
            return False
    return True

nums = input()
alist = nums.split()

for i in range(len(alist)):
    alist[i] = int(alist[i])

for i in range(len(alist)):
    if is_prime(alist[i]) == True:
        print(alist[i])