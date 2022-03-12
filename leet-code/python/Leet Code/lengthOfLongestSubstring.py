class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        dic = {}
        end = len(s)
        j = 0

        for i in range(end):
            #print(output)
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                j = max(j, dic[s[i]] + 1)
                dic[s[i]] = i
            
            output = max(output, i - j + 1)

        return output

a = "au"

s = Solution()
print(s.lengthOfLongestSubstring(a))