class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        mp={}
        # create a dictionary to record the frequency of each char
        for i in nums:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        
        res=[]
        # find the most frequent char and pop the item
        for _ in range(k):
            tmp=max(mp, key=mp.get)
            res.append(tmp)
            mp.pop(tmp)
        
        return res
