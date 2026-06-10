num1 =[1,1,1,2,2,2,2,3,3,4,4,5,5,6,7,8,9,10]
num2 =[2,2,3,4,5,6,7,8,9]

n1 =list(set(num1))
n2 =list(set(num2))
n3=[]
j=0
i=0
# print(list(set(sorted(n2 + n1))))


while i < len(n1) and j < len(n2) :
    if n1[i] < n2[j]:
        n3.append(n1[i])
        i+=1
    elif   n1[i] > n2[j]:
        n3.append(n2[j])
        j+=1
    else :
        n3.append(n1[i])
        i+=1
        j+=1  

while i < len(n1):
    n3.append(n1[i])
    i+=1

while j < len(n2):
    n3.append(n2[j])
    j+=1

print (n3)
