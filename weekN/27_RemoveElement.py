class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # index that will be checked
        k = 0

        for i in range(len(nums)):
            # when encounter safe index
            # (index that is not val)
            if nums[i] != val:
                # update the index that will be checked to the value
                nums[k] = nums[i]
                # move on to the next index that need to be check
                k += 1
        return k
