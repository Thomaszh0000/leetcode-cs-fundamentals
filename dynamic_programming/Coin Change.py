class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        n = amount
        m = length of array coins
        time complexity : O(n * m)
        space complexity : O(n)
        problem : https://leetcode.com/problems/coin-change/
        approach : Keep track of an DP array dp of length amount + 1, 
        which dp[i] means the minimum amount of coins needed in order to bring i up to amount.
        We use an for loop iterated from amount to 0, for each i in for loop, 
        we will assign smallest dp[i + coin] + 1 to dp[i] (for every coin in coins and i + coin need to be smaller or equals to amount). 
        dp[amount] will therefore be initialized to 0 (since we only need 0 when current amount is already equals to target). 
        After iteration, we will return the answer, dp[0].
        """
        dp = [-1] * (amount + 1)
        dp[amount] = 0
        for i in range(amount - 1, -1, -1):
            minC = float('inf')
            for coin in coins:
                if i + coin <= amount:
                    if dp[i + coin] != -1 and dp[i + coin] < minC:
                        minC = dp[i + coin]
            dp[i] = minC + 1 if minC != float('inf') else -1
        return dp[0]
