nums = [1 ,2 ,3 ,3 ,3 ,3 ,3 ,5 ,6 ,8 ,9 ,9 ,10]

target = 18

n = len(nums)
lb =-1
ub =-1
low =0
high = n-1

while low <=high:
    mid = (high + low)//2
    if nums[mid] >= target :
        lb =mid
        high = mid-1
    else:
        low = mid+1
print( lb)


# use the code for the upper bound for the question as a separate loop 