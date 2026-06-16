class Solution:
    def minPartition(self, N):
        # Available denominations in Indian currency
        coins = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
        
        i = 0
        result = []
        total = N
        
        while total > 0:
            if total >= coins[i]:
                # Take the current coin/note
                result.append(coins[i])
                total = total - coins[i]
            else:
                # Move to the next smaller denomination
                i += 1
                
        return result
