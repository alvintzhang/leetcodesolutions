class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        
        def helpfunc(lst, numbers):
            if not numbers: #full permutation
                result.append(lst)
                return
            
            for i in range(len(numbers)):
                new_nums = numbers[:i] + numbers[i+1:]
                helpfunc(lst + [numbers[i]], new_nums)
        
        helpfunc([], nums)
        return result
