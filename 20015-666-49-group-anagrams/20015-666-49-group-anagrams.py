from collections import Counter
class Solution(object):
    def groupAnagrams(self, main):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """ 
        l=[]

        for i in main:
            l.append(dict(Counter(i)))
        check=list()
        for i in l:
            if i not in check:
                check.append(i)
        i=0
        result=list()
        support=list()
        while i != len(check):
            if check[i] in l:
                idx=l.index(check[i])
                support.append(main[idx])
                l[idx]="*"
            else:
                result.append(sorted(support))
                support=list()
                i+=1

        return sorted(result,key=lambda x: len(x))
