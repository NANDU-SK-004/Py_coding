from math import *

def countDig(num):
    return int(log10(num) + 1)

print(countDig(2343))