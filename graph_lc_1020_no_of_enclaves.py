from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # visited[r][c] == 1 means we've seen this land cell in BFS
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()

        # 1. Enqueue all land cells on the border
        for r in range(rows):
            for c in range(cols):
                # Is this cell on the outer border?
                if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                    # If it's land, mark visited and enqueue
                    if grid[r][c] == 1:
                        queue.append((r, c))
                        visited[r][c] = 1

        # 2. BFS to mark all land cells reachable from the border
        while len(queue) != 0:
            i, j = queue.popleft()
            # Explore up, left, down, right
            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_i, new_j = i + x, j + y
                # Skip out-of-bounds
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                # Skip water
                if grid[new_i][new_j] == 0:
                    continue
                # Skip already visited land
                if visited[new_i][new_j] == 1:
                    continue
                # Mark and enqueue this land cell
                queue.append((new_i, new_j))
                visited[new_i][new_j] = 1

        # 3. Count all land cells that were never visited
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    count += 1

        return count
