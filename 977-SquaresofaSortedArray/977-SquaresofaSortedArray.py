class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        lst = []
        for i in nums:
            lst.append(i**2)
        
        lst.sort()
        return lst