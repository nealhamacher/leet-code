class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Using List
        n_str = str(n)
        seen = []
        result = 0
        while result != 1:
            if result in seen:
                return False
            else:
                seen.append(result)
                result = 0
                for digit_char in n_str:
                    digit = int(digit_char)
                    result += digit * digit
                n_str = str(result)
                print(result)
        return True
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(19))
    print(sol.isHappy(2))