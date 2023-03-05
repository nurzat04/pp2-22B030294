import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for x in string.ascii_uppercase:
   with open(x + ".txt", "w") as f:
       f.writelines(x)
