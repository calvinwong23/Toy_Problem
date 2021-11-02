class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

nums = {
    "n_1": 2,
    "n_2": 5
}


s = Solution()
print(s.countBits(nums['n_1'])) # [0,1,1]
print(s.countBits(nums['n_2'])) # [0,1,1,2,1,2]