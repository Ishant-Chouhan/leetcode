class Solution:
    def findDuplicate(self, nums):
        seen = set()
        return next(num for num in nums if num in seen or seen.add(num))

            