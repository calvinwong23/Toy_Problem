class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # output
        output = []

        # Left Accumulation List
        leftAccumulation = [1]

        # Right Accumulation List
        rightAccumulation = [1]

        # Copy and Add 1 to the begining of list
        leftNumsCopy = nums.copy()
        leftNumsCopy.insert(0,1)

        # accumulate left
        tempAccumulation = 1

        for i in range(1, len(leftNumsCopy) - 1):
            tempAccumulation *= leftNumsCopy[i] 
            leftAccumulation.append(tempAccumulation)

        print(leftAccumulation)
        # Copy and Add 1 to the end of list
        rightNumsCopy = nums.copy()
        rightNumsCopy.append(1)
        
        #reset temp
        tempAccumulation = 1
        
        # Accumulate Right
        for j in range(len(rightNumsCopy) - 2, 0, -1):
            tempAccumulation *= rightNumsCopy[j]
            rightAccumulation.append(tempAccumulation)

        # reverse rightAccumulation
        rightAccumulation.reverse()

        # product of leftAccumulation[i] *  rightAccumulation[i]
        for k in range(0, len(nums)):
            output.append(leftAccumulation[k] *  rightAccumulation[k])

        return output

nums = {
    "list_1": [1,2,3,4],
    "list_2": [-1,1,0,-3,3]
}

s = Solution()
print(s.productExceptSelf(nums['list_1'])) #[24,12,8,6]
#print(s.productExceptSelf(nums['list_2'])) #[0,0,9,0,0]
