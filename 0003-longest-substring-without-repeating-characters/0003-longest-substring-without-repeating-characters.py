class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lengths = []

        start = 0
        # end = 0

        max_ = 0
        seen = {}

        for end in range(len(s)):
            if (s[end] in seen) and (seen[s[end]] >= start):
                start = seen[s[end]] + 1
                seen[s[end]] = end
                
                max_ = max(max_, end - start + 1)
            else: 
                seen[s[end]] = end
                max_ = max(max_, end - start + 1)     
            # print(seen)
            # print(max_)       
        
        return max_