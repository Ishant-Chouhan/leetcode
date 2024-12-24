class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        def wordinword(n):
            r1 = "qwertyuiop"
            r2 = "asdfghjkl"
            r3 = "zxcvbnm"
            if n[0] in r1:
                for i in n[1:len(n)]:
                    if i not in r1:
                        return False
                else:
                    return True
            elif n[0] in r2:
                for i in n[1:len(n)]:
                    if i not in r2:
                        return False
                else:
                    return True
            else:
                for i in n[1:len(n)]:
                    if i not in r3:
                        return False
                else:
                    return True
            
        
        return [i for i in words if wordinword(i.lower())==True]