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
        if head == None:
            return False
        temp=head
        l=[]
        while temp != None:
            if id(temp) in l:
                return True
            l.append(id(temp))
            temp=temp.next
        return False
        