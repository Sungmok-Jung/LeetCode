class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lengths = []

        
        i = 0 # start idx
        while i < len(s):
            # print(i)
            result = ""
            dup = False # duplicate idx
            for j in range(i, len(s)):
                # print(j)
                # result.find(s[j])
                
                if (result.find(s[j]) == -1):
                    result += s[j]
                else: # find!
                    i += result.find(s[j]) +1
                    # print(f"find! now, i is {result.find(s[j])+1}")
                    dup = True
                    break
                
            # print(f"result is {result}")
            lengths.append(len(result))
            if dup == False:
                i = len(s)+1 # break from while loop


        
        if len(lengths) > 0:
            return max(lengths)
        else:
            return 0