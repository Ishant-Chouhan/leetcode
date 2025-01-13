class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer=0
        for i in set(s):
            count=s.count(i)
            if count%2==0:
                answer+=2
            else:
                answer+=1
        
        return answer


