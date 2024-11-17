class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        pd=0
        for i in range(len(s)):
            pd += abs(i - t.index(s[i]))
            
        return pd
            