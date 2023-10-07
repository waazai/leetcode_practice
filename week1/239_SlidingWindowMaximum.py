class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        mx=deque()
        res=[]
        for i in enumerate(nums):
            while mx and i[1]>nums[mx[-1]]:
                # pop smaller value from end
                mx.pop()
            mx.append(i[0])
            if i[0]-k>=mx[0]:
                # check front index
                mx.popleft()
            if i[0]+1>=k:
                # start append when reach the size of window
                res.append(nums[mx[0]])
        
        return res
