with open("C:/tsis6/text1.txt", "r") as f, open("C:/tsis6/text2.txt", "w+") as f1:
    for line in f:
        f1.write(line)
    
    