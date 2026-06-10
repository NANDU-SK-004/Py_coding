def func(index ,sum ):
    if sum == target:
        
        return 1
    elif sum >target :
        return 0
    if index >= len(nums):
        return 0
    
    total=sum+nums[index]
    
    pick =func(index+1 ,total)

    total  = sum
    not_pick = func(index +1 ,total)
    return pick + not_pick
    
    
nums =[5 ,9 ,4]

target =9


print(func(0 ,0 ))
