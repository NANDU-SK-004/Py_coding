nums =[1 ,99 ,101 ,98 ,2 ,5 ,3 ,97 ,100 ,0 ,4 ,6 ,96]
# max_count = float("-inf")
# nums.sort()
# count =1
# for i in range(0 ,len(nums)-1):
#     if nums[i+1] -nums[i] == 1:
#         count +=1
#     else:
#         count = 1 
#     max_count =max(max_count ,count)
# print(max_count)
dic ={}
for i in range(0, len(nums)):
    dic.add(nums[i])