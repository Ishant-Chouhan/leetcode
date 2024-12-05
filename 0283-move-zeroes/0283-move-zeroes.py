class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        medium=[]
        i=0
        while True:
            if i==len(nums):
                break
            elif nums[i] == 0:
                medium.append(nums.pop(i))
            else:
                i+=1

        nums.extend(medium)

        return nums
        