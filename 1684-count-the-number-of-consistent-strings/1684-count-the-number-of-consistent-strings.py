class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        s = set(allowed)
        cnt = 0
        for i in words:
            s1=set(i)
            if s1.intersection(s) == s1:
                cnt += 1
        return cnt
            