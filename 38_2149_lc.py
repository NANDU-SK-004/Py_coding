nums =[5,10,-3,-1,-10,6]

result =[0]*len(nums)
k =0
j=1
for num in nums:
    if num > 0 :
        result[k] =num
        k+=2
    else:
        result[j] =num
        j+=2

print(result)