class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

nums = {
    "n_1": [3,0,1],
    "n_2": [0,1],
    "n_3": [9,6,4,2,3,5,7,0,1],
    "n_4": [0]
}

s = Solution()
print(s.missingNumber(nums['n_1'])) # 2
#print(s.missingNumber(nums['n_2'])) # 2
#print(s.missingNumber(nums['n_3'])) # 8
#print(s.missingNumber(nums['n_3'])) # 1
