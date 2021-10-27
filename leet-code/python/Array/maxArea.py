class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # length of input array
        size = len(height)
        
        # two pointers, left init as 0, right init as size-1
        left, right = 0, size-1
        
        # maximal width between leftmost stick and rightmost stick
        max_width = size - 1
        
        # area also known as the amount of water
        area = 0
        
		# trade-off between width and height
        # scan each possible width and compute maximal area
        for width in range(max_width, 0, -1):
            
            if height[left] < height[right]:
                # the height of lefthand side is shorter
                area = max(area, width * height[left] )
                
                # update left index to righthand side
                left += 1
                
            else:
                # the height of righthand side is shorter
                area = max(area, width * height[right] )
                
                # update right index to lefthand side
                right -= 1
                
        return area
                

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

                