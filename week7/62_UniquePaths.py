class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        tb=[]
        for i in range(n):
            r=[]
            for j in range(m):
                r.append(1)
            tb.append(r)
        
        for i in range(1,n):
            for j in range(1,m):
                tb[i][j]=tb[i-1][j]+tb[i][j-1]
        
        return tb[n-1][m-1]
