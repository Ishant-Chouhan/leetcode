class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        c=[]
        for i in range(len(A)):
            Aset=set(A[:i+1])
            Bset=set(B[:i+1])
            c.append(len(Aset.intersection(Bset)))

        return c