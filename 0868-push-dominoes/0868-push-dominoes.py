class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        r=1
        le=len(dominoes)
        l=le-2
        right=dominoes[0]
        left=dominoes[-1]
        while r!=le:
            if dominoes[r]=="." and right[-1]=="R":
                right+="R"
            else:
                right+=dominoes[r]

            if dominoes[l]=="." and left[0]=="L":
                left="L"+left
            else:
                left=dominoes[l]+left
            r+=1
            l-=1

        res=""
        sup=[]
        for i in range(0,len(right)):
            if right[i]==".":
                res+=left[i]
            elif left[i]==".":
                res+=right[i]
            elif right[i]!=left[i]:
                if (right[i+1]==left[i+1]) or (right[i+1]=="." or left[i+1]=="."):
                    sup.append(i)
                    lenght=len(sup)
                    n=lenght//2
                    if lenght%2==0:
                        res+=("R"*n)+("L"*n)
                    else:
                        res+=("R"*n)+"."+("L"*n)
                    sup=[]
                else:
                    sup.append(i)
            else:
                res+=right[i]

        return res