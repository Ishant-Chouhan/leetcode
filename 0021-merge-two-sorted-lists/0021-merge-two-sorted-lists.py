# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #if list
        temp1=list1
        if temp1!=None:
            while temp1.next!=None:
                temp1=temp1.next
            temp1.next=list2
        elif temp1==None and list2!=None:
            return list2
        temp1=list1
        while temp1!=None:
            temp2=temp1.next
            while temp2!=None:
                if temp1.val>temp2.val:
                    temp1.val,temp2.val=temp2.val,temp1.val
                else:
                    temp2=temp2.next
        
            temp1=temp1.next
        
        return list1
        