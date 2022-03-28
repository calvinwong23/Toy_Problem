class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        leftptr = 0         # variable to store left index
        rightptr = len(x)-1 # variable to store right index
    
        # move left index and right index by one unit in each iteration
        while leftptr < rightptr:
        
        # if the digit at left index and digit at right index is not equal,
        # break the loop and and return false
            if x[leftptr] != x[rightptr]:
                return False
            leftptr += 1
            rightptr -= 1
    
        # if the while l
        return True