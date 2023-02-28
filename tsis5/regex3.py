import re
def machtxt(txt):
    x = '^[a-z]+_[a-z]+$'
    if re.search(x,txt):
        return "founded"
    else:
        return "not founded"
print(machtxt("aab_cbbbc"))