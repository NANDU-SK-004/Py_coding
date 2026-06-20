from collections import deque

def bfs ( n ,adj ):
    ans =[]
    queue =deque()
    visited =[0]*n
    
    queue.append(1)
    ans.append(1)
    for i in range(1 ,n+1):
        e =queue.pop()
        for j in range(0 ,len(adj[e])):
            if visited[adj[e][j]] ==0:
                visited[adj[e][j]] =1 
                ans.append(adj[e][j])
            queue.append(adj[e][j])
    print(visited) 
    print(ans)   
    return

n =9
adj =[[],[2,8],[1,3,4],[2],[2,5],[4,6],[5,7],[8,6],[1,7,9],[8]]

bfs (n ,adj)
