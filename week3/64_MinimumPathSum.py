class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # blocks on first row can only go from left
        for i in range (1, len(grid[0])):
            grid[0][i]+=grid[0][i-1]

        # blocks on first column can go come from up
        for i in range(1, len(grid)):
            grid[i][0]+=grid[i-1][0]

        # determine the min path to the rest blocks
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j]+=min(grid[i-1][j], grid[i][j-1]) 

        return grid[-1][-1]       
