class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        lst = s.split(" ")
        print(lst)
        if len(lst)==0:
            return 0
        lst2 = []
        for x in lst:
            if(len(x)!=0):
                lst2.append(x)
        x = lst2[-1]
        return len(x)