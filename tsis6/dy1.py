import os
files = os.listdir() #list all files/dirs
print(files)

for file in files:
    if os.path.isfile(file):
        print(file)