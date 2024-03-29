'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Example 4:
Input: coins = [1], amount = 1
Output: 1

Example 5:
Input: coins = [1], amount = 2
Output: 2
'''
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [sys.maxsize] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if 0 <= i-c < amount+1:
                    dp[i] = min(dp[i], dp[i-c]+1)
        return dp[-1] if dp[-1] != sys.maxsize else -1
