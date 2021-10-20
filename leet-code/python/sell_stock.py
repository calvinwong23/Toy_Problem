class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """


        minProfit = max(prices)
        maxProfit = 0

        for i in range(0, len(prices)):
            print(i,prices[i], minProfit, maxProfit)
            if prices[i] < minProfit:
                minProfit = prices[i]

            elif prices[i] - minProfit > maxProfit:
                maxProfit = prices[i] - minProfit

        return maxProfit

prices = [7,1,5,3,6,4]

s = Solution()
print(s.maxProfit(prices)) #5
