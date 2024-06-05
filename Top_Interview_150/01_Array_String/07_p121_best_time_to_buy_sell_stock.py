class Solution(object):
    # Runtime 715 ms, beats 90.58%. Memory 21.06 MB, beats 15.84%
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] > min:
                current_profit = prices[i] - min
                if current_profit > max_profit:
                    max_profit = current_profit
            else:
                min = prices[i]
        return max_profit


################################################################################
if __name__ == "__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))
    prices = [7,6,5,4,3,2,1]
    print(sol.maxProfit(prices))           