class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        mp=Counter(t)
        n=len(t) # total length neeeded
        wl=l=r=0

        for wr, v in enumerate(s):

            # only decrease total length needed when the char in t appears
            if mp[v]>0: n-=1
            
            # if v in t, decrease the needed amount
            # if v in t and do not need more, decrease the amount to negative
            # if v not in t, mp[v] will be add back to 0 when moving left pointer
            mp[v]-=1

            if n==0: # when window includes all needed chars

                # move left pointer to the first needed char
                # exit loop when s[wl]=0, where left pointer is pointing to a needed char
                while wl<=wr and mp[s[wl]]<0:

                    # if s[wl] not in t, add counter back to 0, left poiter keep sliding
                    # if s[wl] in t but exceed the needed amount, left pointer keep sliding
                    mp[s[wl]]+=1
                    wl+=1
                
                # upadate result if there is no match substring (r==0)
                # or the new result is shorter
                if r==0 or wr-wl <= r-1-l:
                    r, l=wr+1, wl
                
                # left pointer slide forward
                # update the needed strings and total length needed
                mp[s[wl]]+=1
                n+=1
                wl+=1
        
        return s[l:r]
