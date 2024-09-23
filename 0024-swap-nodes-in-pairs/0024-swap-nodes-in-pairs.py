# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp1=head
        if temp1==None:
            return head
        temp2=temp1.next
        while temp2!=None:
            temp1.val,temp2.val=temp2.val,temp1.val
            temp1=temp2.next
            if temp1 == None:
                break
            temp2=temp1.next
            
        
        return head
        