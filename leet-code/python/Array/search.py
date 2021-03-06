class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        for n in nums:
            if n == target:
                return nums.index(n)

        return -1

    def search_Optimization(self, nums, target):

        output = self.binarySearch(nums, target)


        return output

    def binarySearch(self, arr, target):

        start = 0
        end = len(arr) - 1

        while start <= end:
            midpoint = (start + end)//2
            if arr[midpoint] == target:
                return midpoint
            else:
                if target < arr[midpoint]:
                    end = midpoint - 1
                else: 
                    start = midpoint +1

        return midpoint




nums = {
    "list_1": [4,5,6,7,0,1,2],
    "list_2": [4,5,6,7,0,1,2],
    "list_3": [1]
}

target = {
    'target_1': 0,
    'target_2': 3,
    'target_3': 0,
}

s = Solution()
print(s.search(nums['list_1'], target['target_1'])) #4
print(s.search(nums['list_2'], target['target_2'])) #-1
print(s.search(nums['list_3'], target['target_3'])) #-1