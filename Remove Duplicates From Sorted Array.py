class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if(len(nums)==0): 
            return 0

        n = 0
        
        for i in range(1, len(nums)):
            if(nums[i] != nums[n]):
                n+= 1
                nums[n] = nums[i]
        
        return (n + 1)
        
