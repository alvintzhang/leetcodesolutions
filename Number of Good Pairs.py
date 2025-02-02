class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total = 0

        for x in range(len(nums)-1):
            for y in range(x, len(nums)):
                if(nums[x]==nums[y] and x<y):
                    total += 1
        return total
