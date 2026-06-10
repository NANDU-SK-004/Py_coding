nums =[1 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1,1,1,1,0 ,0, 0,0 ,0 ,1,1,1,1,1,1,1,1 ,0 ,0 ,0 ,0 ,0]

count = 0
maxcount = 0
i=0
k=len(nums)
while i < k:
    if nums[i] == 1:
        count+=1
        
    if nums[i] ==0 or i == len(nums)-1 and nums[i-1]==1 and i != 0:
        maxcount =max(maxcount , count)
        count = 0
    i+=1
print(maxcount)