class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        cap=0
        while right > left:
            if cap<min(height[left],height[right])*(right-left):
                    cap=min(height[left],height[right])*(right-left)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return cap
                    
        