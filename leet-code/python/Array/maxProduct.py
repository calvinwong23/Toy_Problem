class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        curMin, curMax = 1,1

        for n in nums:
            if n == 0:
                curMin, curMax = 1,1
                continue

            tmp = curMax*n
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(tmp, n*curMin, n)

            res = max(curMax, curMin, res)

        return res

nums = {
    "list_1": [2,3,-2,4],
    "list_2": [-2,0,-1]
}

s = Solution()
print(s.maxProduct(nums['list_1'])) #6
#print(s.maxProduct(nums['list_2'])) #0
