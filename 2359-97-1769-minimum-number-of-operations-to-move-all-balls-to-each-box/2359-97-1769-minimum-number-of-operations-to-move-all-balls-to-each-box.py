class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        result=[]
        for i in range(len(boxes)):
            count=0
            for j in range(len(boxes)):
                if j<i and boxes[j]=="1":
                    count+=i-j
                elif j>i and boxes[j]=="1":
                    count+=j-i
                else:
                    continue
            result.append(count)
            

        return result