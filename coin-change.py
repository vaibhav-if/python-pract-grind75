class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        print(dp)

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a-c] + 1)
            print(dp)

        return dp[amount] if dp[amount] != (amount + 1) else -1


sol = Solution()
print(sol.coinChange([186,419,83,408], 6249))