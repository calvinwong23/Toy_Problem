class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] > nums[hi]: # go to right
                lo = mid + 1
            elif nums[mid] < nums[lo]: # go to left    
                hi = mid
            else: # [lo, hi] sorted
                return nums[lo]


nums = {
    "list_1": [3,4,5,1,2],
    "list_2": [3,4,5,1,2],
    "list_3": [11,13,15,17]
    
}

s = Solution()
print(s.findMin(nums['list_1'])) #1
#print(s.findMin(nums['list_2'])) #0
#print(s.findMin(nums['list_3'])) #11
