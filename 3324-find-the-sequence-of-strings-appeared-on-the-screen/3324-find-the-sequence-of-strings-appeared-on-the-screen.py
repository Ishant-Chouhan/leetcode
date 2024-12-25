class Solution(object):
    def stringSequence(self, target):
        """
        :type target: str
        :rtype: List[str]
        """
        result = []
        for i in range(len(target)):
            
            s = target[:i]
            j=97
            order = ord(target[i])
            while j <= order:
                result.append(s+chr(j))
                j+=1
                
        return result