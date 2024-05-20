class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        sum = ""
        if len(a) >= len(b):
            long = a
            short = b
        else:
            long = b
            short = a
        for i in range(len(short)):
            d1 = int(a[len(a)-i-1])
            d2 = int(b[len(b)-i-1])
            added = d1 + d2 + carry
            if added == 0:
                sum = "0" + sum
                carry = 0
            if added == 1:
                sum = "1" + sum
                carry = 0
            if added == 2:
                sum = "0" + sum
                carry = 1
            if added == 3:
                sum = "1" + sum
                carry = 1
        for i in range(len(long)-len(short)):
            added = int(long[len(long)-len(short)-i-1]) + carry
            if added == 0:
                sum = "0" + sum
                carry = 0
            if added == 1:
                sum = "1" + sum
                carry = 0
            if added == 2:
                sum = "0" + sum
                carry = 1
        if carry == 1:
            sum = "1" + sum
        return sum

    def addBinaryShort(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """    
        bin_a = int(a, base=2)
        bin_b = int(b, base=2)
        return str(bin(bin_a + bin_b)[2:])

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary("11", "1"))
    print(sol.addBinaryShort("11", "1"))
    print(sol.addBinary("1010", "1011"))
    print(sol.addBinaryShort("1010", "1011"))


