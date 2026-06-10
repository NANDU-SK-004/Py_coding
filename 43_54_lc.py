from math import sqrt
nums=[1,2,3,4,5,6,7,8,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ]

length = int(sqrt(len(nums)))
len = length 
num2 =[[0 for i in range(length)]for i in range(length)]
j =0
k=0
h=0
if len % 2 ==0:
    t=1
else:
    t=0


while(len > 1):
    for i in range (0+h ,length-1-t):
        num2[j][i] = nums[k]
        k+=1

    for i in range (0+h ,length-1 -t):
        num2[i][length-1-h] =nums[k]
        k+=1

    for i in range(length-1 -t ,0 + h,-1):
        num2[length-1 -h][i] = nums[k]
        k+=1

    for i in range (length -1 -t,0+h ,-1):
        num2[i][0+h] =nums[k]
        k+=1
    len -=2
    j+=1
    h+=1
if length % 2 != 0 :
    num2[i][i] =nums[k]
     
print(num2)