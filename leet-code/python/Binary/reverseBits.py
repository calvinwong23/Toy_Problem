class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res    = 0  
        for i in range(32):
            if n&1:
                res += 1 << (31-i)
            n >>= 1
        return res


nums = {
    "n_1": 00000010100101000001111010011100,
    "n_2": 11111111111111111111111111111101
},

s = Solution()
print(s.reverseBits(nums['n_1'])) # 964176192 (00111001011110000010100101000000)
#print(s.reverseBits(nums['n_2'])) # 3221225471 (10111111111111111111111111111111)




