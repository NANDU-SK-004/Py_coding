nums =[17 ,18 ,20 ,1 ,3 ,4 ,5,7,8 ,10 ,11 ,13 ,14 ,15]

n =len(nums)
low =0
high =n - 1
target =8
while low <= high:
    mid = (low+high)//2
    if nums[mid] ==target:
        print (mid)
    if nums[low] == nums[mid] == nums[high]:
          low+=1
          high-=1
          continue
    if nums[mid] <= nums[high]:
        if nums[mid] <= target <=nums[high]:
                low =mid +1
        else:
                high =mid-1
    else:
        if nums[low] <= target <=nums[mid]:
                high =mid -1
        else:
                low =mid+1