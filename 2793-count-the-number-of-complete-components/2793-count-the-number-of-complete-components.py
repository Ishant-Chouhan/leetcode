class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        support=[]
        for i in range(n):
            support.append({i})

        for i in edges:
            edge0=i[0]
            edge1=i[1]
            support[edge0].add(edge1)
            support[edge1].add(edge0)

        result=[]
        for i in support:
            if i not in result:
                result.append(i)
        ans=0
        print(result)
        for s in result:
            if all(s.isdisjoint(other) for other in result if other != s):
                ans+=1

        return ans

        
            




