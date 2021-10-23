class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


nums = {
    "list_1": [3,4,5,1,2],
    "list_2": [3,4,5,1,2],
    "list_3": [11,13,15,17]
    
}

s = Solution()
print(s.findMin(nums['list_1'])) #1
#print(s.findMin(nums['list_2'])) #0
#print(s.findMin(nums['list_3'])) #11
