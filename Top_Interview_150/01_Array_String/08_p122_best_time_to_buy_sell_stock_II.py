class Solution(object):
    # Runtime 39 ms, beats 47.95%. Memory 12.75 MB, beats 59.58%
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            current_profit = 0
            if i == len(prices) - 1:
                current_profit = prices[i] - min_price
            if prices[i] < prices[i-1]:
                current_profit = prices[i-1] - min_price
                min_price = prices[i]
            profit += current_profit
        return profit
    
    # Runtime 31 ms, beats 92.15%. Memory 12.84 MB, beats 34.24%
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] >= prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit


################################################################################

if __name__ == "__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))
    print(sol.maxProfit2(prices))
    prices = [1,2,3,4,5]
    print(sol.maxProfit(prices))
    print(sol.maxProfit2(prices))

