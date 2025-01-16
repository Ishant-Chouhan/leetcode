class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ans=""
        for i in range(len(strs[0])):
            temp=""
            for j in strs:
                temp += j[i]
            sortedtemp="".join(sorted(temp))
            if temp!=sortedtemp:
                ans+="1"

        return len(ans)