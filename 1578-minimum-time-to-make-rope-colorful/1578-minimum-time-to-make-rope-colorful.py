class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        time=0
        i=0
        while i != len(colors):
            a=colors[i]
            j=i+1
            while j != len(colors) and colors[j]==colors[i] :
                j+=1

            time+=sum(neededTime[i:j])-max(neededTime[i:j])
            i=j

        return time