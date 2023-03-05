from time import sleep
import math
def suspend(function, miliseconds, *args):
    sleep(miliseconds/1000)
    return function(*args)
print(suspend(lambda x: math.sqrt(x), 100, 16))
print(suspend(lambda x: math.sqrt(x), 1000, 100))
print(suspend(lambda x: math.sqrt(x), 2000, 25100))
