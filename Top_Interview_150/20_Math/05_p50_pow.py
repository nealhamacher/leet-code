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
    
    def myPow2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Base cases
        if n == 0:
            return 1
        if n == 1:
            return x
        
        # Account for negative exponents
        if n < 0:
            return 1/self.myPow2(x, -n)
        
        # Recursive case
        if n % 2 == 0:
            return self.myPow2(x*x, n//2)
        else:
            return self.myPow2(x*x, n//2) * x
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2, 10))
    print(sol.myPow(2.1, 3))
    print(sol.myPow(2, -2))
    print(sol.myPow2(2, 10))
    print(sol.myPow2(2.1, 3))
    print(sol.myPow2(2, -2))
        
        