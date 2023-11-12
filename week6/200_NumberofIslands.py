class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """ 

        def traverse(c,r):
            if not(0<=c<len(grid) and 0<=r<len(grid[0])): return
            if grid[c][r]=="0": return
            grid[c][r]="0"
            for (x,y) in ((0,1),(1,0),(0,-1),(-1,0)):
                traverse(c+x, r+y)
        
        ct=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    # if encounter land, increase counter
                    # then traverse around and make the whole land water
                    traverse(i,j)
                    ct+=1
        
        return ct
