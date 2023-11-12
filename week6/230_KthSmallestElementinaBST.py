# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        stk=[]
        while root or stk:

            # put the nodes in stack
            # the last item in stack will be the smallest
            while root:
                stk.append(root)
                root = root.left

            # get the current smallest
            root=stk.pop()
            k-=1
            if k==0:
                return root.val

            # track the right branch
            root = root.right




