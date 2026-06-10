nums =[1 ,0 ,-1 ,5 ,-2 ,2 ,0 ,9]
n = len(nums)
# li =[0]*4

# f_set =set()
# for i in range(0 ,l):
#     for j in range(i+1 ,l):
#         hash_map =set()
#         for k in range(j+1 ,l):
#             fourth =0 -(nums[i]+nums[j]+nums[k])
#             if fourth in hash_map :
#                 li =[nums[i] ,nums[j] ,nums[k] ,fourth]
#                 li.sort()
#                 f_set.add(tuple(li)) 
#             hash_map.add(nums[k])
# print(f_set)
target =0
ans =[]
nums.sort()
for i in range (0 ,n):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    for j in range (i+1 ,n):
        if j > i+1 and nums[j] == nums[j - 1]:
            continue
        k =j+1
        l= n-1
        while k<l:
            total =nums[i] + nums[j] +nums[k] +nums[l]
            if total == target :
                ans.append([nums[i] , nums[j] ,nums[k] ,nums[l]])
                k+=1
                l-=1
                while k < l and nums[k] == nums[k-1]:
                    k+=1
                while l> k and nums[l] == nums[l+1]:
                    l -=1
            elif total < target:
                k+=1
            else :
                l-=1
print(ans)