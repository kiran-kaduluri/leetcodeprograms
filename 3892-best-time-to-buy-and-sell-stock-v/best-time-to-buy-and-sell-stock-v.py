from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            best_buy = -prices[0]
            best_sell = prices[0]

            for i in range(1, n):
                # normal transaction
                dp[t][i] = prices[i] + best_buy

                # short selling
                dp[t][i] = max(dp[t][i], best_sell - prices[i])

                # carry forward
                dp[t][i] = max(dp[t][i], dp[t][i - 1])

                # ✅ FIX: use i-1 to avoid same-day overlap
                best_buy = max(best_buy, dp[t - 1][i - 1] - prices[i])
                best_sell = max(best_sell, dp[t - 1][i - 1] + prices[i])

        return dp[k][n - 1]
