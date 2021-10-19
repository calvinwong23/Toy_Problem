class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        d = {}

        for i in range(len(nums)):
            temp = target - nums[i]

            if temp in d:
                return [d[temp], i]
            else:
                d[nums[i]] = i


list_input = {
    "list_1": [2,7,11,15],
    "list_2": [3,2,4],
    "list_3": [3,3],
}

target_input = {
    'target_1': 9,
    'target_2': 6,
    'target_3': 6,
}

s = Solution()
print(s.twoSum(list_input['list_1'], target_input['target_1']))
print(s.twoSum(list_input['list_2'], target_input['target_2']))
print(s.twoSum(list_input['list_3'], target_input['target_3']))