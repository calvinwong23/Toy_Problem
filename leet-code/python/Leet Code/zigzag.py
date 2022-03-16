class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        res = []
        x = 0
        direction = 1

        if numRows == 1:
            return s

        for m in range(numRows):
            res.append([])

        for i in range(len(s) -1):
            print(res)
            
            if x == 0:
                res[x][y] = s[i]
                x += 1
            elif x == numRows - 1:
                x-= 1
                y += 1
                res[x][y] = s[i] 
                
        return res

a = 'PAYPALISHIRING'
s = Solution()
#print(s.convert(a, 3))

b = [['','']]
b[0][0] = a[0]
b[0][1] = a[1]

print(b)

