class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maximum = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                width = j - i  
                tempheight = min(height[i], height[j])
                if (width*tempheight)> maximum:
                    maximum = width*tempheight
        
        return maximum
