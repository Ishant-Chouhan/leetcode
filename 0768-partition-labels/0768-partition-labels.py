class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        length=len(s)
        checked=[]
        idxs=[]
        for i in range(len(s)):
            x=s[i]
            if x not in checked:
                checked.append(x)
                idxs.append([i,length-s[::-1].index(x)-1])
        print(idxs)
        i=0
        while i<len(idxs)-1:
            if idxs[i][1]>idxs[i+1][0]:
                idxs[i]=[idxs[i][0],max(idxs[i][1],idxs[i+1][1])]
                idxs.pop(i+1)
            else:
                i+=1
        print(idxs)
        for i in range(len(idxs)):
            idxs[i]=idxs[i][1]-idxs[i][0]+1

        return idxs
