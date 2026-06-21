from copy import deepcopy
from collections import deque

class Solution:
    def matr(self, input):
        matrr = deepcopy(input) 
        count =0
        queue = deque()
        
        
        for i in range(len(matrr)):
            for j in range(len(matrr[0])):
                if matrr[i][j] == 1:
                    count+=1
                    queue.append((i ,j))

        if count == 0:
            return matrr
        elif count == len(matrr)*len(matrr[0]):
            return matrr
        

        
        
        
        return queue
        




input =[[0,1,0],[0,0,1],[0,1,1]]

a =Solution()

print(a.matr(input ))