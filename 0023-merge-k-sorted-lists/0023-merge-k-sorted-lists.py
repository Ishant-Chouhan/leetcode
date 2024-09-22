# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, list):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if len(list)==0:
            return None
        
        temp1=list[0]
        
        head=temp1
        
        for i in range(1,len(list)):
            
            if (temp1!=None and list[i]==None) or (temp1==None and list[i]==None) :
                continue
                
            elif temp1==None and list[i]!=None:
                temp1=list[i]
                head=temp1
                
            else:
                while temp1.next!=None:
                    temp1=temp1.next
                temp1.next=list[i]

        temp1=head
            
        while temp1!=None:
                
            temp2=temp1.next
                
            while temp2!=None:
                    
                if temp1.val>temp2.val:
                    temp1.val,temp2.val=temp2.val,temp1.val
                    temp2=temp2.next
                        
                else:
                    temp2=temp2.next
        
            temp1=temp1.next
        
            
        return head
            