import re
def machtxt(txt):
    x = '^a(b*)$'
    if re.search(x, txt):
        return("founded")
    else:
        return("not founded")
print(machtxt("abbba"))
print(machtxt("abb"))