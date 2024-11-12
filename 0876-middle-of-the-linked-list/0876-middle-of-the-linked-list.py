# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head
        length=0
        while temp != None:
            length+=1
            temp = temp.next
            
        temp = head
        
        for i in range(length//2):
            temp = temp.next
            
        head = temp
        return head