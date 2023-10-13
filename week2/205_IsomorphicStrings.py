class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # hash map
        mp={}

        for i in range(len(s)):

            if s[i] not in mp: 
                if t[i] not in mp.values():
                    # create a new hash when char from both str are new
                    mp[s[i]] = t[i]
                else:
                    # when char from "t" is already in hash 
                    # but char from "s" does not match
                    return False

            if mp[s[i]]!=t[i]: 
                # when char from "t" does not match the hash map
                return False
        

        return True
