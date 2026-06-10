nums =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# row =len(nums)
# column =len(nums[0])

# num2 =[[0 for i in range(column)]for i in range (row)]
# k=0
# for i in range(0 ,row):
#     for j in range(0 ,row):
#         num2[k][j] = nums[row -1 -j][k]
#     k+=1

# nums = num2
# print(nums)


# THE ABOVE TAKES EXTRA SPACE 
for i in range(0 ,len(nums)):
    for j in range (0 ,len(nums)):
        nums[i][j] = nums[j][i]   #TAKING TRANSPOSE  

for i in range(0 ,len(nums)):
    nums[i].reverse()               #TAKING REVERSE OF TRANSPOSE GIVE DESIRED OP 
print(nums)