class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        Stype=0
        for i in jewels:
            Stype+=stones.count(i)
        return Stype