class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lengths = []
        
        for i in range(len(s)):
            result = ""
            for j in range(i, len(s)):
                if (s[j] not in result):
                    result += s[j]
                else:
                    # lengths.append(len(result))
                    break
            lengths.append(len(result))
            result = ""

        if len(lengths) > 0:
            return max(lengths)
        else:
            if s == " ":
                return 1
            else:
                return 0