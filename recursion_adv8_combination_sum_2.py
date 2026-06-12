def back(index ,total ,subset):
    if total == 0:
        result.append(subset.copy())
        return
    if total < 0:
        return
    if index > len(nums):
        return
    for i in range (index ,len(nums)):
        if i > index and nums[i] == nums[i-1]:
            continue
        subset.append(nums[i])
        sum =total - nums[i]
        back(i+1 ,sum ,subset)
        subset.pop()

result =[]
subset =[]
nums =[1 ,1 ,1 ,2 ,2 ]
back(0 ,4 ,subset)
print(result)