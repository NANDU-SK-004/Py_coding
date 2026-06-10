num =[1,4,2,5,3,1,4,2,1,1,5,3,6]
num2=[4,5,2,3,2,1,3,1,4,5,3,4,2]

hash ={}
for n in num:
    hash[n] = hash.get(n ,0)+1

print(hash)