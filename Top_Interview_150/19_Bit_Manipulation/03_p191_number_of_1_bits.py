class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for digit in bin(n):
            if digit == '1':
                count += 1
        return count
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(11))
    print(sol.hammingWeight(128))
    print(sol.hammingWeight(2147483645))