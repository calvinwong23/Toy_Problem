class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        #res = [[ "" for _ in range(numRows)]]
        res =""
        l = len(s)
        step=2*numRows-2

        print(res)

        for i in range(numRows):
            for j in range(0,l-i,step):
                res+=s[i+j]
                if i!=0 and i!=numRows-1 and j+step-i<l:
                    res+=s[j+step-i]

                
        return res

a = 'PAYPALISHIRING'
s = Solution()
print(s.convert(a, 3))


#res = [[] for _ in range(3)]
#res[0][0] = "a"
#print(res)

