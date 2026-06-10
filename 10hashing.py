num =[1,4,2,5,3,1,4,2,1,1,5,3,6]
num2=[4,5,2,3,2,1,3,1,4,5,3,4,2]

arr = [0]*7

print(arr)
for n in num:
    arr[n] = arr[n] + 1

print(arr)

for n in num2:
    if n < 1 or n > 7:
        print(0)
    else:
        print( n  , arr[n])    
