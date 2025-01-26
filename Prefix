class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = ""
        first = strs[0]
        for i in range(len(strs[0])):
            temp = (first[i:i+1])
            for j in strs:
                if(i>=len(j)):
                    return prefix
                else if (j[i:i+1]!=temp):
                    return prefix
            prefix+=temp
        return prefix
        
