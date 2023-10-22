# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        res = ListNode(None)
        ptr = res
        q = PriorityQueue()

        # puts values in priorty queue to sort
        for i in lists:
            if i != None:
                q.put((i.val, i))
        
        while q.qsize()>0:
            # pop queue to build list
            ptr.next=q.get()[1]

            # refill the queue with the next value from linklist
            ptr=ptr.next
            if ptr.next!=None:
                q.put((ptr.next.val, ptr.next))
        
        # return next since the head is 0
        return res.next
