class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return 0
        s=0
        s1=0
        for i in range(len(nums)+1):
            s+=i
        for i in nums:
            s1+=i
        return s-s1

nums = {
    "n_1": [3,0,1],
    "n_2": [0,1],
    "n_3": [9,6,4,2,3,5,7,0,1],
    "n_4": [0]
}

s = Solution()
print(s.missingNumber(nums['n_1'])) # 2
#print(s.missingNumber(nums['n_2'])) # 2
#print(s.missingNumber(nums['n_3'])) # 8
#print(s.missingNumber(nums['n_3'])) # 1
