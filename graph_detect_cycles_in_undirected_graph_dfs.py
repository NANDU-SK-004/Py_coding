class Solution:
    def dfs(self, node, parent, visited, adj_list):
        # Mark the current node as visited
        visited[node] = 1
        
        # Explore all neighbors
        for adjNode in adj_list[node]:
            # If neighbor not visited, recurse
            if visited[adjNode] == 0:
                if self.dfs(adjNode, node, visited, adj_list):
                    return True
            # If neighbor visited and not the parent, cycle found
            elif adjNode != parent:
                return True
        
        # No cycle found along this path
        return False

    def isCycle(self, V, edges):
        # Build adjacency list
        adj_list = [[] for _ in range(V)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = [0] * V  # 0 = unvisited, 1 = visited
        
        # Try DFS from each unvisited vertex
        for i in range(V):
            if visited[i] == 0:
                # If DFS finds a cycle, return True immediately
                if self.dfs(i, -1, visited, adj_list):
                    return True
        
        # No cycle found in any component
        return False
