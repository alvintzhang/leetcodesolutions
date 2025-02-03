class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maximum = 0

        while(left < right):
            width = right - left
            tempheight = min(height[left], height[right])
            maximum = max(maximum, width * tempheight)

            if(height[left] < height[right]):
                left += 1
            else:
                right = right-1

        return(maximum)
