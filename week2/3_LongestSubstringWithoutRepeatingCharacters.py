class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        mp={}  # dictionary for seen characters
        l=mx=0

        for r, c in enumerate(s):
            if c in mp and mp[c]>=l:
                # slide left pointer to the next once encounter repreated char
                l=mp[c]+1
            
            # record the index of seen char
            mp[c]=r
            mx=max(r+1-l, mx)
        
        return mx
