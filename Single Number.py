class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        temp = []
        for i in nums:
            if i in temp:
                temp.remove(i)
            else:
                temp.append(i)
        
        return temp[0]
