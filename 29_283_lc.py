nums =[2,3,4,5,0,0,0,0,0,0,9,9,8,7,6,5,6,7,0,0,0,0,0]

n= nums.count(0)
for _ in range(n):
    nums.remove(0)
    nums.append(0)
        

print(nums)

    
