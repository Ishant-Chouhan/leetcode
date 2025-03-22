class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel="aeiouAEIOU"
        s=list(s)
        low = 0
        high = len(s)-1
        while low<high:
            print(low,high)
            if s[low] in  vowel and s[high] in vowel:
                s[low],s[high]=s[high],s[low]
                low+=1
                high-=1
            elif s[low] in  vowel and s[high] not in vowel:
                high-=1
            elif s[low] not in  vowel and s[high] in vowel:
                low+=1
            else:
                low+=1
                high-=1

        return "".join(s)
            
