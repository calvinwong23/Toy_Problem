class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == -b:
            return 0
        if abs(a) > abs(b):
            a, b = b, a
        if a < 0:
            return -self.getSum(-a, -b)
        while b:
            c = a & b
            a ^= b
            b = c << 1
        return a

s = Solution()
print(s.getSum(1,2)) #3
print(s.getSum(2,3)) #5