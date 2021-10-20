class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        

nums = {
    "list_1": [1,2,3,4],
    "list_2": [-1,1,0,-3,3]
}

s = Solution()
print(s.productExceptSelf(nums['list_1'])) #[24,12,8,6]
print(s.productExceptSelf(nums['list_2'])) #[0,0,9,0,0]
