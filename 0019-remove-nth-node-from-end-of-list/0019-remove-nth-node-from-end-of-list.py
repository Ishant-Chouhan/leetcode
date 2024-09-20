# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp=head
        while temp.next!=None:
            temp=temp.next
        last=temp
        temp=head
        if head.next==None and n==1:
            head=None
        else:
            while n!=1:
                if temp.next==last:
                    last=temp
                    temp=head
                    n-=1
                    continue
                else:
                    temp=temp.next
            while temp.next!=last and temp!=last:
                temp=temp.next
            temp.next=last.next
            if last==head:
                head=head.next
            last.next=None
        
        return head
        
        
        