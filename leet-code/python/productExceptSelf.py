class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = []
        

        for i in range(len(nums)):
            skip = nums[i]
            for j in range(len(nums)):
                if nums[j] == skip:
                    continue
                else:
                    total = total * nums[j]
            output.append(total)

        return output

nums = {
    "list_1": [1,2,3,4],
    "list_2": [-1,1,0,-3,3]
}

s = Solution()
print(s.productExceptSelf(nums['list_1'])) #[24,12,8,6]
print(s.productExceptSelf(nums['list_2'])) #[0,0,9,0,0]
