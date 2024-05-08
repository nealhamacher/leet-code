class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        root = 1
        while (root*root) <= x:
            root +=1
        return root - 1


################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))
    print(sol.mySqrt(8))
    print(sol.mySqrt(63))
    print(sol.mySqrt(64))
    print(sol.mySqrt(65))
    print(sol.mySqrt(120))
    print(sol.mySqrt(121))
    print(sol.mySqrt(122))
    print(sol.mySqrt(169))