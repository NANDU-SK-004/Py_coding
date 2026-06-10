nums =[1 ,2 ,3]

n =len(nums)
result =[ ]
sub = 1<<n
for num in range (0 , sub):
    lst =[]
    for i in range (0 ,n):
        if num & (1 << i) != 0:
            lst.append(nums[i])
    result.append(lst)
print(result)