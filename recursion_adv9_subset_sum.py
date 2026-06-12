def back(index ,total):
    if index >= len(nums):
        result.append(total)
        return
    sum = total + nums[index]
    back(index+1 ,sum)
    sum = sum - nums[index]
    back(index +1 ,sum)



result =[]
nums =[5 ,9 ,3]
back(0 ,0)

print(result)