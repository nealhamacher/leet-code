class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = str(n)
        return int(n[::-1], 2)
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(00000010100101000001111010011100))
    print(sol.reverseBits(11111111111111111111111111111101))