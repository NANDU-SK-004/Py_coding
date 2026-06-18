from collections import deque

class Solution:
    def isCycle(self, V, edges):
        # 1. Build adjacency list
        adj_list = [[] for _ in range(V)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [0] * V  # 0 = unvisited, 1 = visited

        # 2. For each vertex, if unvisited, start BFS
        for i in range(V):
            if visited[i] == 1:
                continue

            queue = deque()
            queue.append((i, -1))  # (node, parent)
            visited[i] = 1

            # 3. Standard BFS loop
            while queue:
                node, parent = queue.popleft()
                # 4. Check all neighbors
                for adjNode in adj_list[node]:
                    if visited[adjNode] == 0:
                        visited[adjNode] = 1
                        queue.append((adjNode, node))
                    else:
                        # If visited and not the parent, it's a cycle
                        if adjNode != parent:
                            return True

        # 5. No cycle found
        return False
