class Solution:
    def solve(self, index, jump, lastIndex, nums):
        if index >= lastIndex:
            return jump
        minJump = float("inf")
        for i in range(1, nums[index] + 1):
            minJump = min(minJump, self.solve(index + i, jump + 1, lastIndex, nums))
        return minJump

    def jump(self, nums: List[int]) -> int:
        return self.solve(0, 0, len(nums) - 1, nums)



class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        left = 0
        right = 0
        while right < n - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            jumps += 1
        return jumps
