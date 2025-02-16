class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        x = nums
        lst = []
        for i in range(len(nums)):
            lst.append(0)
            for j in x:
                if(nums[i]>j):
                    lst[i]+=1
        return lst
