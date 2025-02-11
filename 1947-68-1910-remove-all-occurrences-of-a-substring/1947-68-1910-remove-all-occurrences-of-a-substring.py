class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        n=len(part)
        lens=len(s)
        while part in s:
            idx=s.index(part)
            s=s[:idx]+s[idx+n:lens]

        return s