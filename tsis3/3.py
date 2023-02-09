def solve(numheads, numlegs):
    for i in range(numlegs + 1):
        j = numheads - i
        if 2*i + 4*j == numlegs:
            print(i, j)

solve(35, 94)