class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""

        for i in range(len(s)):
            # this is for odd length palindrome
            
            word1 = self.checkPalindrome(s, i, i)
            print(word1)

            # this is for even length palindrome
            word2 = self.checkPalindrome(s, i, i+1)
            print(word2)

            #word1 will be max length word from word1 and word2
            if len(word1) >= len(word2):
                word1 = word1
            else:
                word1 = word2

            # compare word1 with our result
            if len(word1) >= len(result):
                result = word1
            else:
                result = result

        return result
    
    def checkPalindrome(self,s, lo, hi):
        # expand as long as 'lo' can grow to the left
        # and 'hi' and grow to the right and chracters at those index match
        
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1

        # return the slice from original string that starts from our last matched index of lo and hi. We don't increament hi because python slice goes up to ending index-1
        return s[lo+1:hi]

a = "racecar"

s = Solution()
print(s.longestPalindrome(a))
#print(s.checkPalindrome(a,1,1))
#print(s.checkPalindrome(a,0,0))