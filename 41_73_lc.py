nums =[[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]
rows =set()
columns=set()
for i in range(0 ,len(nums)):
    for j in range (0 ,len(nums[0])):
        if nums[i][j] == 0:
            rows.add(i)
            columns.add(j)              #adding values to set

for i in rows:
    for j in range(0 ,len(nums[0])):
        nums[i][j] =0

for j in columns:
    for i in range(0 ,len(nums)):
        nums[i][j] =0

print(nums)