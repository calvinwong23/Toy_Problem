class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxSub = nums[0]
        curSum = 0
        
        for n in nums:
            #print(n)
            if curSum < 0:
                curSum = 0
            curSum += n

            maxSub = max(curSum, maxSub)
        return maxSub


        

nums = {
    "list_1": [-2,1,-3,4,-1,2,1,-5,4],
    "list_2": [-2,1],
    "list_3": [5,4,-1,7,8]
}

s = Solution()
print(s.maxSubArray(nums['list_1'])) #6
print(s.maxSubArray(nums['list_2'])) #1
print(s.maxSubArray(nums['list_3'])) #23