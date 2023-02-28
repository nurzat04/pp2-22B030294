import re
txt = "hello zoe, happy birthday to you."
print(re.sub("[ ,.]", ":", txt))