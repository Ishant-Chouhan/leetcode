class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings)<=1:
            return len(ratings)
        l1=[1]
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                l1.append(l1[i-1]+1)
            else:
                l1.append(1)
                
        l2=[1]
        ratings.reverse()
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                l2.append(l2[i-1]+1)
            else:
                l2.append(1)
        candy=0
        l2.reverse()
        for i in range(len(ratings)):
            candy+=max(l1[i],l2[i])
            
        return candy