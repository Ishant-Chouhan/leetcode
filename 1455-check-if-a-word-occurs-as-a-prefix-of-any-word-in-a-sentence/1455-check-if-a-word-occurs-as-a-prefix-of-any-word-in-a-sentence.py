class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        sentence=sentence.split()
        for i in sentence:
            if searchWord in i and i.find(searchWord) == 0:
                return sentence.index(i)+1
        else:
            return -1
        