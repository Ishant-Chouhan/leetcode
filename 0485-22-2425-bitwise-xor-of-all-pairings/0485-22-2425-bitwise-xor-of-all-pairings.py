class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        len1=len(nums1)
        len2=len(nums2)
        a=len1%2==0
        b=len2%2==0
        if a and b:
            return 0
        elif a:
            ans=0
            for i in nums1:
                ans^=i
            return ans
        elif b:
            ans=0
            for i in nums2:
                ans^=i
            return ans
        else:
            nums1.extend(nums2)
            ans=0
            for i in nums1:
                ans^=i
            return ans
            