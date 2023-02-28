import re
def matchtxt(txt):
    x = '[A-Z]+[a-z]+$'
    if re.search(x,txt):
        return "founded"
    else:
        return "not founded"
print(matchtxt("aaaA"))
print(matchtxt("AaBbGg"))