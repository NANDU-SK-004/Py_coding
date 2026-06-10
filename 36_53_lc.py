

# sum = 0
# sum2 = 0

# for i in range (0 , len(nums)):
#     for j in range (i ,len(nums)):
#         # for k in range (i ,j+1):
#         sum = sum + nums[j]
#         sum2=max(sum ,sum2)
#     sum =0
# print(sum2)

nums= [-2 ,1 ,-3 ,4 ,-1 ,2 ,1 ,-5 ,4]

max_val =float("-inf")
tot =0
for i in range (0 ,len(nums)):
    tot = tot + nums[i]

    if tot > max_val:
        max_val =tot
    if tot < 0:
        tot =0
print(max_val)