# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def GCD(a,b):
            
            if max(a,b) % min(a,b) ==0:
                return min(a,b)
            
            c=1
            for i in range(2,(min(a,b) //2)+1):
                if a%i==0 and b%i==0 and i>c:
                    c=i
            return c
        
        if head.next == None :
            return head
        temp1=head
        temp2=temp1.next
        while temp2 != None:
            temp1.next=ListNode(GCD(temp1.val,temp2.val),temp2)
            temp1=temp2
            temp2=temp2.next
            
        return head
        