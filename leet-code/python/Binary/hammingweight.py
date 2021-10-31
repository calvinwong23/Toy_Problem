class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

num = {
    "n_1": "00000000000000000000000000001011",
    "n_2": "00000000000000000000000010000000",
    "n_3": "11111111111111111111111111111101" 
}

s = Solution()
print(s.hammingWeight(num['n_1'])) # 3
#print(s.hammingWeight(num['n_2'])) # 1
#print(s.hammingWeight(num['n_3'])) # 31