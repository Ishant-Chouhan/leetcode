class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        length = len(s)
        if length < k:
            return False
        odd=0
        for i in set(s):
            if s.count(i) % 2 !=0:
                odd+=1
        if odd<=k:
            return True    
        return False