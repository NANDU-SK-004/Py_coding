class Solution:
    def solve(self, node):
        # 1. Base case: an empty subtree has height 0
        if node is None:
            return 0
        
        # 2. Recurse on left and right
        leftHeight  = self.solve(node.left)
        rightHeight = self.solve(node.right)
        
        # 3. Current node's height = 1 + taller subtree
        return 1 + max(leftHeight, rightHeight)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.solve(root)
