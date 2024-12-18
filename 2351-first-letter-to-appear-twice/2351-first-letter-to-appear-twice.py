class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        support = []
        for i in s:
            if i in support:
                return i
            support.append(i)        