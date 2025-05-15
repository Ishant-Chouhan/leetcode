class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        i=1
        while i<len(groups):
            if groups[i]==groups[i-1]:
                words.pop(i)
                groups.pop(i)
            else:
                i+=1

        return words
