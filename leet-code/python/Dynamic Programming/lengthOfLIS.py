class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return 0

        seql = [0]*len(nums)
        seql[0] = 1
        maxl = 1
        for i in range(1,len(nums)):
            this_maxl = 1
            for j in range(0, i):
                if nums[j]<nums[i]:
                    if seql[j]+1 > this_maxl:
                        this_maxl = seql[j]+1
            seql[i] = this_maxl
            if seql[i] > maxl:
                maxl = seql[i]
        return maxl
        