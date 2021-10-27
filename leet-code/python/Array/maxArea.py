class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

height = {
    "list_1": [1,8,6,2,5,4,8,3,7],
    "list_2": [1,1],
    "list_3": [4,3,2,1,4],
    "list_4": [1,2,1]
}

s = Solution()
print(s.maxArea(height['list_1'])) #49
#print(s.maxArea(height['list_2'])) #1
#print(s.maxArea(height['list_3'])) #16
#print(s.maxArea(height['list_4'])) #2

                