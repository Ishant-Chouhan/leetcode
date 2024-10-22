class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s=s.lower()
        for i in s:
            if i.isalnum() == False:
                print(i)
                s=s.replace(i,"")
        print(s)
        return s==s[::-1]
                
        