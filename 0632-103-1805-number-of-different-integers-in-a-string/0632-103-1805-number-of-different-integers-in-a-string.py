class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        temp=""
        for i in word:
            if i in "1234567890":
                temp+=i
            else:
                temp+=" "
        temp=temp.split()
        for i in range(len(temp)):
            temp[i]=int(temp[i])

        return len(set(temp))
