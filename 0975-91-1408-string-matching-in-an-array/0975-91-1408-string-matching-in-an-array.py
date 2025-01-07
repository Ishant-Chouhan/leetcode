class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result=[]
        for i in range(len(words)):
            wordi=words[i]
            for j in range(len(words)):
                wordj=words[j]
                if i!=j and wordj in wordi:
                    result.append(wordj)
                else:
                    continue
        return list(set(result))