import re
def machtxt(txt):
    x = 'ab{2,3}'
    if re.search(x,txt):
        return "founded"
    else:
        return "not founded"
print(machtxt("abbb"))