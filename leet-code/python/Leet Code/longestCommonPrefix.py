class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''
        shortest = min(strs, key = len)
        for i in range(len(shortest)):
            if sum(1 for s in strs if shortest[i] != s[i]) > 0:
                return shortest[:i]
            
        return shortest
        

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
#print(s.checkPalindrome(a,1,1))
#print(s.checkPalindrome(a,0,0))

