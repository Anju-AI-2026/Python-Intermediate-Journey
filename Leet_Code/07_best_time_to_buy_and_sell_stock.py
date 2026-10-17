
# LeetCode #121 - Best Time to Buy and Sell Stock


class Solution:

    def maxProfit(self, prices):

        minimum_price = prices[0]
        maximum_profit = 0

        for price in prices:

            if price < minimum_price:
                minimum_price = price

            profit = price - minimum_price

            if profit > maximum_profit:
                maximum_profit = profit

        return maximum_profit


solution = Solution()

print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(solution.maxProfit([7, 6, 4, 3, 1]))     # 0
