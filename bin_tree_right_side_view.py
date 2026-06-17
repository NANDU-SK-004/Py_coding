#BFS

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # If it's the last node at this level, add it to result
                if i == level_size - 1:
                    result.append(node.val)

                # Push children into queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


#DFS
class Solution:
    def dfs(self, node, depth, result):
        if not node:
            return

        # If this depth is being visited for the first time, add node
        if depth == len(result):
            result.append(node.val)

        # Visit right child first, then left child
        self.dfs(node.right, depth + 1, result)
        self.dfs(node.left, depth + 1, result)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, 0, result)
        return result
