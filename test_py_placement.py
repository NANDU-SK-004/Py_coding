#n queens

class Solution(object):
    def solveNQueens(self, n):
            grid = [["."]*n for i in range (n)]
            sol =[]
            cols =set()
            pos_dia =set()
            neg_dia =set()
            def backtrack(r):
                if r ==n:
                    sol.append(["".join(row) for row in grid]) # from grid we take each row  ,as converting to single list is happening here
                    return
                for c in range(n):
                    if c in cols or r+c in pos_dia or r-c in neg_dia:
                        continue
                    cols.add(c)
                    pos_dia.add(r+c)
                    neg_dia.add(r-c)
                    grid[r][c] ="Q"

                    backtrack(r+1)
                    cols.remove(c)
                    pos_dia.remove(r+c)
                    neg_dia.remove(r-c)
                    grid[r][c] ="."
            backtrack(0)
            return sol
                  