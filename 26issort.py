nums =[1 ,2 ,3 ,4 ,5, 6, 7, 10 ,9]
n =len(nums)
for i in range (0 ,n-1):
    if nums[i+1] < nums[i]:
        print("not sorted")
        break
else :    
        print("sorted")