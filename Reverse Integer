class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        posneg = 1
        if(x<0):
            posneg = (-1)
        x = abs(x)
        digits = []

        while x > 0:
            digits.insert(0, x % 10)  
            x //= 10
        
        digits.reverse()

        print(digits)

        total = 0

        a = len(digits)-1
        i = 0 
        while(a>=0):
            if(total + ((digits[a])*(10**i))>(2**31-1)):
                return 0
            else:
                total += digits[a]*(10**i)
                a = a-1
                i +=1

        return total*posneg
        
