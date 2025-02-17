class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices)==0):
            return 0
        
        mn = float('inf')
        mx = 0            
        
        for i in prices:
            if(i<mn):
                mn = i
            elif(i-mn > mx):
                mx = i-mn 
        
        return(mx)