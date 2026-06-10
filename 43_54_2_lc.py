from math import sqrt



nums = [1,2,3,4,5,6,7,8,9]
n= int(sqrt(len(nums)))

num2 = [[0 for _ in range(n)] for _ in range(n)]

layer = 0
k = 0
remaining = n

while remaining > 1:

    for i in range(layer, n - 1 - layer):
        num2[layer][i] = nums[k]
        k += 1

    for i in range(layer, n - 1 - layer):
        num2[i][n - 1 - layer] = nums[k]
        k += 1

    for i in range(n - 1 - layer, layer, -1):
        num2[n - 1 - layer][i] = nums[k]
        k += 1

    for i in range(n - 1 - layer, layer, -1):
        num2[i][layer] = nums[k]
        k += 1

    remaining -= 2
    layer += 1

if n % 2 == 1:
    center = n // 2
    num2[center][center] = nums[k]

for row in num2:
    print(row)