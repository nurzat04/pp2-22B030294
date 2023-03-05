#fp = open("C:/tsis6/text3.txt", "w")
import os
print('Exist:', os.access('C:/tsis6', os.F_OK))
print(os.path.exists('C:/tsis6'))
os.remove("C:/tsis6/text3.txt")