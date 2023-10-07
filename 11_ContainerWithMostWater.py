class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)
        mx = 0
        pt1= 0
        pt2 = n-1

        while pt2>pt1:
            h = min(height[pt1], height[pt2]) # the max height that can hold water
            l = pt2 - pt1
            if height[pt1]>height[pt2]:  # keep the higher edge
                pt2 -=1
            else:
                pt1+=1
            if mx < h*l:
                mx=h*l
        
        return mx
