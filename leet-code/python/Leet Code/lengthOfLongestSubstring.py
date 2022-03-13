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

    def slidingWindow(self, s):
        end = len(s)
        res = 0
        mp = {}
        l = 0
        for j in range(end):
            if s[j] in mp:
                l = max(mp[s[j]], l)
        
            res = max(res, l - j + 1)
            mp[s[j]] = j + 1

        return res
a = "au"

s = Solution()
#print(s.lengthOfLongestSubstring(a))
print(s.slidingWindow(a))