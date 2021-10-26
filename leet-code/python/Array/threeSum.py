class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        

nums = {
    "list_1": [-1,0,1,2,-1,-4],
    "list_2": [],
    "list_3": [0]
    
}

s = Solution()
print(s.threeSum(nums['list_1'])) #[[-1,-1,2],[-1,0,1]]
#print(s.threeSum(nums['list_2'])) #[]
#print(s.threeSum(nums['list_3'])) #[]
