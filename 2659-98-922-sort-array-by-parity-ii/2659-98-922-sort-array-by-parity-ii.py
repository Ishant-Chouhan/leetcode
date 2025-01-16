class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even=[]
        odd=[]
        nums.sort()
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)

        nums=list()
        for i in range(len(even)):
            nums.append(even[i])
            nums.append(odd[i])

        return nums
