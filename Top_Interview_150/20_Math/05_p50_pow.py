class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1/self.myPow(x, -n)
        
        return self.myPow(x*x, n-1)
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.1, 3))
        
        