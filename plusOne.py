class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        string = ''.join(map(str, digits))
        
        temp = int(string)
        temp+=1
        cur = str(temp)
        lst = [int(x) for x in cur]
        return lst
