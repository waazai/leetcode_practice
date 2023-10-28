class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # (index until, prefix)
        q = collections.deque([(-1, 0)])
        res = len(nums)+1
        pfx = 0

        for i, n in enumerate(nums):
            pfx+=n

            if n>0: # positive case
                while q and pfx-q[0][1]>=k:
                    # trace from first index prefix
                    res = min(res, i-q.popleft()[0])

            else: # negative case
                while q and pfx<=q[-1][-1]:
                    # pop if the encounter prefix is larger
                    q.pop()

            q.append((i, pfx))
        
        return -1 if res>len(nums) else res
