class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfits = 0

        l = 0
        r = l + 1

        while l < r and r < len(prices):
            profit = prices[r] - prices[l]
            maxProfits = max(maxProfits, profit)

            if prices[r] < prices[l]:
                l = r

            r += 1

        return maxProfits