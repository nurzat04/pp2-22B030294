import re
txt = "HelloZOEhappyBIRthday"
print(re.findall('[A-Z][^A-Z]*', txt))