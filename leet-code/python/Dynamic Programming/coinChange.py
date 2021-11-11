class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        
        dp = [0]+[math.inf]*amount
        coins = sorted(coins)
        for i in range(1,amount+1):
            if i >= coins[0]:
                dp[i] = 1+min(dp[i-j] for j in coins if j <= i)
        return dp[-1] if dp[-1]<=amount else -1