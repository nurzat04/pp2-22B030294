import re
def matchtxt(txt):
    x = 'a.*?b$'
    if re.search(x,txt):
        return "founded"
    else:
        return "not founded"
print(matchtxt("aaaA"))
print(matchtxt("AAAaavbb"))