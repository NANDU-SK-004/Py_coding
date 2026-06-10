nums =[7 ,2,10 ,1 ,10 ,6 ,5 ,17 ,0]


# max_diff = float("-inf")
# diff =0
# for i in range(0 ,len(nums)):
#     for j in range(i ,len(nums)):
#         if nums[i] < nums[j]:
#             diff = nums[j] -nums[i]
#         max_diff =max(max_diff,diff)
#         diff =0
# print(max_diff)    
min_diff = float("-inf")
least =nums [0]
for i in range (0 ,len(nums)-1):
    least = min(least ,nums[i])
    diff = nums[i] - least
    min_diff= max(min_diff ,diff)
print(min_diff)