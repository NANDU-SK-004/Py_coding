

def func(index ,subset):
    if index >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[index])
    func(index+1 ,subset)
    subset.pop()
    func(index+1 ,subset)

result =[]
subset =[]
nums =[9,7,6]
func(0 ,subset)

print(result)
