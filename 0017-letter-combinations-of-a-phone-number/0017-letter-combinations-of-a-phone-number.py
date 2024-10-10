class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def iter_n(l,n,d):
            if len(l)==0:
                l.extend(d[n])
            else:
                for i in range(len(l)):
                    l.append(l.pop(0)+n)
            
            return l
                
        d={"":[],
        "2":["a","b","c"],
        "3":["d","e",'f'],
        "4":["g","h",'i'],
        "5":["j","k",'l'],
        "6":["m","n",'o'],
        "7":["p","q",'r',"s"],
        "8":["t",'u',"v"],
        "9":["w",'x',"y","z"]}
        
        if len(digits) <= 1:
            return d[digits]
        op=[]
        result=[]
        if len(op)==0:
            op.extend(d[digits[0]])
        for i in map(lambda a : d[a] ,digits[1:len(digits)]):
            for j in op:
                for k in i:
                    result.append(j+k)
            op=result
            result=[]
                    
        return op