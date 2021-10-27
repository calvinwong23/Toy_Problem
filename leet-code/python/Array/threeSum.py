class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for count, value in enumerate(nums):
            if count > 0 and value == nums[count -1]:
                continue

            l, r = count + 1, len(nums)-1
            while l < r:
                threeSum = value + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append ([value, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1

        return res



nums = {
    "list_1": [-1,0,1,2,-1,-4],
    "list_2": [],
    "list_3": [0] 
}

s = Solution()
print(s.threeSum(nums['list_1'])) #[[-1,-1,2],[-1,0,1]]
#print(s.threeSum(nums['list_2'])) #[]
#print(s.threeSum(nums['list_3'])) #[]
