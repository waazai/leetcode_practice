# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # return [] if no nodes
        if root==None:
            return []
        
        ans = [[root.val]]
        chld = [root]
        while len(chld)>0:
            chld, ls = self.cur_lv(chld)
            if len(ls)>0: ans.append(ls)

        return ans
    
    # traverse current level
    def cur_lv(self, nds):
        chld=[]
        lv_nd=[]
        for i in nds:
            if i.left!=None:
                chld.append(i.left)
                lv_nd.append(i.left.val)
            if i.right!=None:
                chld.append(i.right)
                lv_nd.append(i.right.val)
        return chld, lv_nd
