def func(index ,sum ,subset):
    if sum == target:
        final.append(subset.copy())
        return
    elif sum >target :
        return
    if index >= len(nums):
        return
    subset.append(nums[index])
    total=sum+nums[index]
    
    func(index+1 ,total,subset)
    e =subset.pop()
    total -=e

    func(index +1 ,total ,subset)
    
nums =[5 ,9 ,4]
subset =[]
target =9
final =[]

func(0 ,0 ,subset)
print(final)

