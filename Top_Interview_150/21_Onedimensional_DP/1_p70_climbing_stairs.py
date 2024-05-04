class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        table=[None] * n
        table[0] = 1
        table[1] = 2
        table[2] = 3
        for i in range(3, n):
            table[i] = table[i-1] + table[i-2]
        return table[n-1]
        


################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(3))
    print(sol.climbStairs(4))
    print(sol.climbStairs(6))
    # n = 1, 1 solution
    # n = 2, 2 solution
    # n = 3, 3 solution
        # 1 + 1 + 1
        # 2 + 1
        # 1 + 2
    # n = 4, 5 solutions 
        # 1 + 1 + 1 + 1
        # 2 + 1 + 1
        # 1 + 2 + 1
        # 1 + 1 + 2
        # 2 + 2
    # n = 5, 8 solutions
        # 1 + 1 + 1 + 1 + 1
        # 2 + 1 + 1 + 1
        # 1 + 2 + 1 + 1
        # 1 + 1 + 2 + 1
        # 1 + 1 + 1 + 2
        # 2 + 2 + 1
        # 2 + 1 + 2
        # 1 + 2 + 2
    # n = 6, 13 solutions
        # 1 + 1 + 1 + 1 + 1 + 1
        # 2 + 1 + 1 + 1 + 1
        # 1 + 2 + 1 + 1 + 1
        # 1 + 1 + 2 + 1 + 1
        # 1 + 1 + 1 + 2 + 1
        # 1 + 1 + 1 + 1 + 2
        # 2 + 2 + 1 + 1
        # 2 + 1 + 2 + 1
        # 2 + 1 + 1 + 2
        # 1 + 2 + 2 + 1
        # 1 + 2 + 1 + 2
        # 1 + 1 + 2 + 2
        # 2 + 2 + 2 