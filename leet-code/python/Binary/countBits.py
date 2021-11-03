class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        iniArr = [0]
        if n > 0:
            amountToAdd = 1
            while len(iniArr) < n + 1:
                iniArr.extend([x+1 for x in iniArr])
        
        return iniArr[0:n+1]

nums = {
    "n_1": 2,
    "n_2": 5
}


s = Solution()
print(s.countBits(nums['n_1'])) # [0,1,1]
print(s.countBits(nums['n_2'])) # [0,1,1,2,1,2]