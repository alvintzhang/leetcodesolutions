class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(0 not in nums):
            return 0
        nums.sort()
        print(nums)
        for x in range(len(nums)-1):
            temp = nums[x]
            print(temp)
            nextvar = nums[x+1]
            print(nextvar)

            if(temp+1!=nextvar):
                return temp+1

        return nums[-1]+1
