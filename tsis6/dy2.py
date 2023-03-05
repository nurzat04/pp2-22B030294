fp = open('text1.txt', 'a+')
print("hello world1", file=fp)
import os
print('Exist:', os.access('C:\tsis6\text1.txt', os.F_OK))
print('Readable:', os.access('C:\tsis6\text1.txt', os.R_OK))
print('Writable:', os.access('C:\tsis6\text1.txt', os.W_OK))
print('Executable:', os.access('C:\tsis6\text1.txt', os.X_OK))