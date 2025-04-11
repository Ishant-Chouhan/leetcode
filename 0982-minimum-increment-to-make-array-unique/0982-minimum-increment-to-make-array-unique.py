class Solution:
    def minIncrementForUnique(self, nums):
        min_increments = 0

        nums.sort()

        for i in range(1, len(nums)):
            # Ensure each element is greater than its previous
            if nums[i] <= nums[i - 1]:
                # Add the required increment to minIncrements
                min_increments += nums[i - 1] + 1 - nums[i]
                 

                # Set the element to be greater than its previous
                nums[i] = nums[i - 1] + 1

        return min_increments