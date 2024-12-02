class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        prefix=[i for i in words if s.find(i)==0]
        
        return len(prefix)