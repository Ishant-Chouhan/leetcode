class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        if len(s)%2!=0:
            return False
        #initializing variables
        wildcard=0
        opening=0 #count for opening bracket
        closing=0 #count for closing bracket
        
        #traversing left ro right
        for i in range(len(locked)):
            if locked[i]=="0":
                wildcard+=1
            else:
                if s[i]=="(":
                    opening+=1
                else:
                    closing+=1

            if wildcard + opening < closing:
                return False

        wildcard=0
        opening=0 
        closing=0

        #reversing both string to traverse right to left
        s=s[::-1]
        locked=locked[::-1]

        for i in range(len(locked)):
            if locked[i]=="0":
                wildcard+=1
            else:
                if s[i]=="(":
                    opening+=1
                else:
                    closing+=1

            if wildcard + closing < opening:
                return False

        return True
