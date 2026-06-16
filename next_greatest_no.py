# nums =[19 ,4 ,2 ,11 ,6 ,5 ,3 ,10]
# top =-1
# ans =[-1]*len(nums)
# j =0
# s =[]
# for i in range (len(nums)-1 ,-1 ,-1):
#     if s[top] == None:
#         s.push(nums[i])
#         continue
#     elif nums[i] < s[top]:
#         ans[i] = s[top]
#     else :
#         while s[top] <= nums[i]:
#             s.pop()
#             s.push(nums[i])
# print(ans)

nums = [19, 4, 2, 11, 6, 5, 3, 10]
ans = [-1] * len(nums)
s = []
for i in range(len(nums) - 1, -1, -1):

    while s and s[-1] <= nums[i]:
        s.pop()

    if s:
        ans[i] = s[-1]
    s.append(nums[i])

print(ans)