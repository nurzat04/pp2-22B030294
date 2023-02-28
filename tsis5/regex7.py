import re
def snake_to_camel(txt):
    return ''.join(x.capitalize() or '_' for x in txt.split('_'))
print(snake_to_camel("hello_zoe"))