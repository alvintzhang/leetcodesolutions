class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        substring = ""
        maxlength = 0

        if(len(s) == 1):
            return(1)

        for i in range(len(s)):
            if s[i] in substring:

                maxlength = max(maxlength, length)

                index = substring.index(s[i])
                substring = substring[index + 1:]
                length = len(substring)

            substring += s[i]
            length += 1


        maxlength = max(maxlength, length)

        return maxlength

            
