class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = []
        for i in s:
            if i not in temp :
                temp.append(i)
        for i in temp:
            if s.count(i)==1:
                return s.index(i)
        else:
            return -1