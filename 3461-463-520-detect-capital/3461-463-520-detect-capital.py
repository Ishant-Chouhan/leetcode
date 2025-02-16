class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return upper(word)==word or lower(word)==word or upper(word[0])+lower(word[1:len(word)])==word