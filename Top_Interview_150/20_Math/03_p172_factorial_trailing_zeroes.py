class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        return n // 5 + self.trailingZeroes(n // 5)
    

################################################################################
if __name__ == "__main__":
    sol = Solution()
    print(sol.trailingZeroes(3))
    print(sol.trailingZeroes(5))
    print(sol.trailingZeroes(25))