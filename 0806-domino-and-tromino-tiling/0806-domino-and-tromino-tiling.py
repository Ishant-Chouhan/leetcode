class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        elif n==1:
            return 1
        elif n==2:
            return 2
        elif n==3:
            return 5
        else:
            mod = 10**9 + 7
            arr = [0] * (n+1)
            arr[0],arr[1],arr[2],arr[3] = 1,1,2,5

            for i in range(4,n+1):
                arr[i] = (arr[i-1] * 2 + arr[i-3]) % mod

            return arr[n]
        