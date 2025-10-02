class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lengths = []

        
        i = 0 # start idx
        while i < len(s):
            result = ""
            dup = False # duplicate idx
            for j in range(i, len(s)):
                
                find = result.find(s[j])
                
                if (find == -1):
                    result += s[j]
                else: # find!
                    i += find + 1
                    dup = True
                    break
                
            lengths.append(len(result))
            if dup == False:
                i = len(s)+1 # break from while loop

        if len(lengths) > 0:
            return max(lengths)
        else:
            return 0

test = Solution()
s = "abcabcbb"
answer = test.lengthOfLongestSubstring(s)
print(answer)