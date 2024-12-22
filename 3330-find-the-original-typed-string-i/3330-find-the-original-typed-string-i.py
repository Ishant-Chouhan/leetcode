class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        possible = 1
        
        for i in range(1,len(word)):
            if word[i] == word[i-1]:
                possible += 1
            
        return possible