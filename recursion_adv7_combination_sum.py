class Solution:
    def solve (self ,index ,total ,subset ,nums ,target ,result):
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        if index >= len(nums):
            return
        Sum = total +nums[index]
        subset.append(nums[index])
        self.solve (index ,Sum,subset ,nums ,target ,result)
        Sum = total
        subset.pop()
        self.solve (index +1 ,Sum,subset ,nums ,target ,result)

k = Solution()
result =[]
k.solve(0 ,0 ,[] ,[2 ,3 ,6 ,7], 7,result )
print( result)        