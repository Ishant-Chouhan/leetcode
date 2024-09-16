# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        temp1=l1
        temp2=l2
        c=[]
        a=0
        while (temp1 != None) or (temp2 != None):
            if temp1==None:
                if temp2.val + a >=10:
                    c.append((temp2.val + a)%10)
                    a=((temp2.val + a)-((temp2.val + a) % 10)) //10
                else:
                    c.append(temp2.val + a)
                    a=0
                temp2=temp2.next
            elif temp2==None:
                if temp1.val + a >=10:
                    c.append((temp1.val + a)%10)
                    a=((temp1.val + a)-((temp1.val + a) % 10)) //10
                else:
                    c.append(temp1.val + a)
                    a=0
                temp1=temp1.next
            else:
                if temp1.val + temp2.val + a >=10:
                    c.append((temp1.val + temp2.val + a)%10)
                    a=((temp1.val + temp2.val + a)-((temp1.val + temp2.val + a) % 10)) //10
                else:
                    c.append(temp1.val + temp2.val + a)
                    a=0
                temp1=temp1.next
                temp2=temp2.next
        
        if a!=0:
            c.append(a)

        temp3=ListNode(c[0])
        l=temp3
        temp4=temp3
        for i in range(1,len(c)):
            l.next=ListNode(c[i])
            l=l.next
        
        return temp4