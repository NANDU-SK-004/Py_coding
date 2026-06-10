nums =[5 ,1 ,3 ,3 ,7 ,1 ,7]
k=nums[0]
for i in range(1 , len(nums)):
    k=k^ nums[i]
print (k)