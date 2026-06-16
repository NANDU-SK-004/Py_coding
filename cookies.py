class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g)
        m = len(s)
        
        # Sort greed factors and cookie sizes
        g.sort()
        s.sort()
        
        left = 0   # Pointer for children
        right = 0  # Pointer for cookies
        count = 0  # Number of satisfied children
        
        # Assign cookies greedily
        while left < n and right < m:
            if g[left] <= s[right]:   # If cookie satisfies the child's greed
                count += 1            # Child is content
                left += 1             # Move to next child
            right += 1                # Move to next cookie
        
        return count
