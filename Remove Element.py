class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        for i in range(len(nums)):
            if val not in nums:
                return len(nums)
            else:
                nums.remove(val)
        
        return len(nums)
        
