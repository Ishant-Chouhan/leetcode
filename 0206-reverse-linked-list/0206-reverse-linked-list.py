# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        back = None
        current = head
        
        while current != None :
            
            front = current.next
            current.next = back
            back = current
            current = front
            
            
        head = back
        return head
        