from math import tan, pi
n_sides = int(input(""))
s_length = int(input(""))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print(p_area)