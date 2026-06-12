def back(index ,total ,subset ,count):
    if count == size:
        if total == 0:
            result.append(subset.copy())
        return
    if index >= len(nums):
        return
    sum = total - nums[index]
    subset.append(nums[index])
    count+=1
    back ( index + 1 , sum ,subset ,count )
    subset.pop()
    count-=1
    sum = total
    back( index+1 ,sum ,subset ,count)
        







size =3
nums = [1,2,3,4,5,6,7,8,9]
set=[]
result =[]

back(0 ,9,set ,0)

print(result)