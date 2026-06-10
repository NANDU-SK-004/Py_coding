nums =[17 ,18 ,20 ,1 ,3 ,4 ,5,7,8 ,10 ,11 ,13 ,14 ,15]

n =len(nums)
low =0
high =n - 1
mini =float("inf")
while low <= high:
    mid = (low+high)//2
    if nums[mid] <= nums[high] :
        mini =min(mini ,nums[mid])
        high =mid -1
    else:
        mini =min(mini ,nums[mid])
        low =mid+1
print(mini)            
