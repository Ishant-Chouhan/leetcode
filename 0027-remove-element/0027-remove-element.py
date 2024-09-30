class Solution(object):
    def removeElement(self, nums, val):
        if len(nums)==0:
            return 0
        k=0
        i=0
        while i!=len(nums):
            if nums[i]==val:
                nums.pop(i)
                nums.append("_")
            elif nums[i]=="_":
                break
            else:
                i+=1
                k+=1
        return k
        