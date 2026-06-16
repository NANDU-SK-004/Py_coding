class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0  # farthest index we can reach

        for i in range(len(nums)):
            if i > max_index:
                # if we are at an index we cannot reach
                return False
            # update the farthest index reachable
            max_index = max(max_index, i + nums[i])

        return True
