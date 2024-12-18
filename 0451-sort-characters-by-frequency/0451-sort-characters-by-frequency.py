class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp=[]
        for i in s:
            if i not in temp:
                temp.append(i)
        counts=[]
        for i in temp:
            counts.append(s.count(i))
        s=""
        while temp !=[]:
            maximum = max(counts)
            idx = counts.index(maximum)
            s += temp[idx] * maximum
            counts.pop(idx)
            temp.pop(idx)
            
            
        return s
            