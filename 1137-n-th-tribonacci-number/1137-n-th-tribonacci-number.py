class Solution:
    def tribonacci(self, n):
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1

        trib = [-1]*(n+1)
        trib[0] = 0
        trib[1] = 1
        trib[2] = 1
        def Trib(idx):
            if trib[idx] == -1: 
                if trib[idx-1] == -1: trib[idx-1] = Trib(idx-1) 
                if trib[idx-2] == -1: trib[idx-2] = Trib(idx-2) 
                if trib[idx-3] == -1: trib[idx-3] = Trib(idx-3)            
                return  trib[idx-1] + trib[idx-2] + trib[idx-3]
            else:    
                return trib[idx]
        return Trib(n)    