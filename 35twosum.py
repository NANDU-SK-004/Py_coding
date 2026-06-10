nums= [5,9,1,2,4,15,6,3]

n = int(input("enter the number to search :"))

# for i in nums:
#     if (n-i) in nums :
#         print(f"the numbers are {i} and {n-i}")

k ={}

for i in range (len(nums)):
    if (n-nums[i]) in k:
        print(k.get(n-nums[i]) , i)
    k[nums[i]] = i
     
