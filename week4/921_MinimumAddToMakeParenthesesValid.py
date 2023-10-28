class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """

        
        l=r=0
        for i in s:
            if i == '(':
            # need a move when there is a '('
                l+=1
            else:
                if l==0:
                # needs a move when there is a ')'
                # but no corresponding '('
                    r+=1
                else:
                # cancel out a move when there is a ')'
                    l-=1
        
        return r+l
