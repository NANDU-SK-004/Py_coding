from collections import deque
from copy import deepcopy
from typing import list

class Solution :
    def orange_rotten(self ,grid):
        row =len(grid)
        col =len(grid[0])
        grid_copy =deepcopy(grid)
        queue =deque()

        for r in range(row):
            for c in range(col):
                if grid_copy[r][c] == 2:
                    queue.append((r,c))
                if grid_copy[r][c] == 1:
                    fresh_count +=1

        minutes =0

        while queue and fresh_count >0: #for validity
            minutes +=1
            total_rotten =len()

            for _ in range(len(queue)):              # for the endof queue
                i ,j = queue.popleft()
                
                for di ,dj in [(1,0),(-1 ,0),(0 ,1),(0 ,-1)]:
                    new_i ,new_j =  i+di ,j+dj                      #for the each traversal
                    if new_i <0 or new_i == row or new_j <0 or new_j ==col:
                        continue
                    if grid_copy[new_i][new_j] == 0 or grid_copy[new_i][new_j]== 2:
                        continue
                    fresh_count -=1
                    grid_copy[new_i][new_j] =2
                    queue.append((new_i ,new_j))