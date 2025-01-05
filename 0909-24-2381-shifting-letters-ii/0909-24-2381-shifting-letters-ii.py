class Solution:
    def shiftingLetters(self, s, shifts):
        '''hm = defaultdict(int)
        for i in shifts:
            start,end,dir = i
            for j in range(start,end+1):
                if dir == 0:
                    hm[j] -= 1
                else:
                    hm[j] += 1
        res = ""
        for i in range(len(s)):
            res += chr((ord(s[i]) - ord('a') + hm[i]) % 26 + ord('a'))
        return res'''
        #the above code gives me TLE, SO we have to think of another approach where we can reduce the no.of iterations

        n = len(s)
        pre = [0] * (n+1)
        for start,end,direc in shifts:
            pre[start] += (1 if direc == 1 else -1)
            if end + 1 < n:
                pre[end+1] -= (1 if direc == 1 else -1)
        res = ""
        curr = 0
        for i in range(len(s)):
            curr += pre[i]
            res += chr((ord(s[i])-ord('a') + curr) % 26 + ord('a'))
        return res


        

        
        