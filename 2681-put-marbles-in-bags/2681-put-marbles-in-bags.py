class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        partitions=list()
        for i in range(len(weights)-1):
            partitions.append(weights[i]+weights[i+1])

        scores=sorted(partitions)
        res = 0
        for i in range(k - 1):
            res += scores[-1 - i] - scores[i]
        return res