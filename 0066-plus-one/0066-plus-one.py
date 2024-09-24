class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        for i in digits:
            s+=str(i)
        s=str(eval(s)+1)
        digits=[]
        for i in s:
            digits.append(eval(i))
        return digits

        