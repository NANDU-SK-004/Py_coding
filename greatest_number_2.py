nums = [19, 4, 2, 11, 6, 5, 3, 10]
n = len(nums)

ans = [-1] * n
s = []

for i in range(2 * n - 1, -1, -1):
    idx = i % n

    while s and s[-1] <= nums[idx]:
        s.pop()

    if i < n:
        if s:
            ans[idx] = s[-1]

    s.append(nums[idx])

print(ans)