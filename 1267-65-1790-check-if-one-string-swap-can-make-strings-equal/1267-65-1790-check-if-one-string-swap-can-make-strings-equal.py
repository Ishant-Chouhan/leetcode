
class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        elif set(s1) != set(s2):
            return False
        print("Start")
        count=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count+=1
            elif s1.count(s1[i])!=s2.count(s1[i]):
                return False
            if count>2:
                return False
        else:
            return True
            
        