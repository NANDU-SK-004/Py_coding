num = 898  
final = num
total =0

while num > 0:
    k = num % 10
    total=total*10 + k
    num = num // 10

if final == total :
    print ("palindrome")
else :
    print ("not palindrome")
