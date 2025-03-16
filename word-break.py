class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                # print(s[j:i])
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]

sol = Solution()
print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))