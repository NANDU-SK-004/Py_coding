# from copy import deepcopy
# from collections import deque

# class Solution:
#     def matr(self, input):
#         matrr = deepcopy(input) 
#         count =0
#         queue = deque()
#         matrr2 =deepcopy(input)
#         val =True
        
#         for i in range(len(matrr)):
#             for j in range(len(matrr[0])):
#                 if matrr[i][j] == 1:
#                     count+=1
#                     queue.append((i ,j))

#         if count == 0:
#             return matrr
#         elif count == len(matrr)*len(matrr[0]):
#             return matrr
#         while queue:
#             i ,j = queue.popleft()
#             dupli(i ,j)
#             def dupli(i ,j):
            
#                 count =1
#                 for dx ,dy in ((-1 ,0),(0 ,-1),(1 ,0),(0 ,1)):
#                     if i+dx < 0 or i+dx >len(matrr) or j+dy < 0 or j+dx > len(matrr[0]):
#                         continue
                    
#                     if matrr[i+dx][j+dy] == 0:
#                         matrr2[i][j] =count
#                         break
#                     val =False
                        
#                 if val == False:
#                     for dx ,dy in ((-1 ,0),(0 ,-1),(1 ,0),(0 ,1)):
#                         if i+dx < 0 or i+dx >len(matrr) or j+dy < 0 or j+dx > len(matrr[0]):
#                             continue
#                         if matrr[i+dx][j+dy] ==1:
#                             matrr2[i][j] =count+dupli(i+dx ,j+dy)
                    

        
        
        
#         return 
        




# input =[[0,1,0],[0,0,1],[0,1,1]]

# a =Solution()

# print(a.matr(input ))

from collections import deque

class Solution:
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))

        return mat