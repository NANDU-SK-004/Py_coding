from math import *
num = 153  
final = num
total =0

while num > 0:
    k = num % 10
    total=total + pow(k,3);                 #instead of 3 give len(str(num))
    num = num // 10
print(total)
if final == total :
    print ("armstrong")
else :
    print ("not armstrong")
