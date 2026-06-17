# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

from collections import deque

class Solution:
    def topView(self, root):
        if not root:
            return []
        
        # dictionary to store first node for each horizontal distance
        hd_map = {}
        
        # queue for BFS -> stores (node, horizontal_distance)
        q = deque([(root, 0)])
        
        while q:
            node, hd = q.popleft()
            
            # store the first node we encounter at this HD
            if hd not in hd_map:
                hd_map[hd] = node.data
            
            # add left and right children with updated HD
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        
        # extract results sorted by horizontal distance
        result = [hd_map[key] for key in sorted(hd_map.keys())]
        return result
