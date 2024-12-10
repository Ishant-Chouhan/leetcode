class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp=""
        count=1
        for i in s:
            if i in temp:
                print(temp)
                count+=1
                temp=i
            else:
                temp+=i
                
        return count