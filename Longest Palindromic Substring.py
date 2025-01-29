class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        mlength = 0
        mstr = ""

        if(len(s)==1):
            return s

        for i in range(len(s)):
            

            for j in range(i+1, len(s)):
                temp = s[i:j+1]

                palin = True
                for x in range(len(temp)//2):
                    left = temp[x]
                    right = temp[len(temp)-x-1]
                    if(left!=right): 
                        palin = False
                        break
                        


                    
                if(palin):
                    if(len(temp)>mlength):
                        mlength=len(temp)
                        mstr = temp
                        
        if(mstr == "" and len(s)>0):
            return(s[0:1])
        return mstr
