class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1=s[::-1]
        len_s1=len(s1)
        result = 0
        count=[i for i in set(s) if s.count(i)>1]
        for i in count:
            first_idx = s.index(i)
            last_idx = len_s1-1-s1.index(i)
            result += len(set(s[first_idx + 1 : last_idx]))

        return result
