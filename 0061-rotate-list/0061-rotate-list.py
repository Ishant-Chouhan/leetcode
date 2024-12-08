# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==0 or head ==None:
            return head
        temp=head
        
        count=1
        while temp.next != None:
            count+=1
            temp=temp.next
            
        temp.next=head
        temp=head
        if k>=count:
            k=k%count
        for i in range(count-k-1):
            temp=temp.next
            
        head=temp.next
        temp.next=None
        
        return head
            
            


        