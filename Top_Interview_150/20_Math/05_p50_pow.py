class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        pow = x
        while n > 1:
            pow *= x
            n -= 1
        return pow
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2, 10))
    print(sol.myPow(2.1, 3))
    print(sol.myPow(2, -2))
        
        