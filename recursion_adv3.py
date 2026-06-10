def func(index ,sum ,subset):
    if sum == target:
        
        return True
    elif sum >target :
        return False
    if index >= len(nums):
        return False
    subset.append(nums[index])
    total=sum+nums[index]
    
    pick =func(index+1 ,total,subset)
    if pick ==True:
        return True
    e =subset.pop()
    total  = sum
    not_pick = func(index +1 ,total ,subset)
    return not_pick
    
    
nums =[5 ,9 ,4]
subset =[]
target =9
final =[]

print(func(0 ,0 ,subset))


