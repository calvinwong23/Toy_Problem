class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nums.sort()
        prev = 0
        start = 1
        end = len(nums) - 1

        while start <= end:
            if nums[prev] == nums[start]:
                return True
            
            prev += 1
            start += 1

        return False

list_input = {
    "list_1": [1,2,3,1],
    "list_2": [1,2,3,4],
    "list_3": [1,1,1,3,3,4,3,2,4,2]
}

s = Solution()
print(s.containsDuplicate(list_input['list_1'])) #true
print(s.containsDuplicate(list_input['list_2'])) #false
print(s.containsDuplicate(list_input['list_3'])) #true