class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        
        # compare 2 nodes is enough
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]
