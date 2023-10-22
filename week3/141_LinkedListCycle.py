# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ls=[]
        ptr=head
        # trace through the link list and record visited nodes
        while ptr!=None:
            if ptr in ls: return True
            else:
                ls.append(ptr)
                ptr=ptr.next

        return False
            
