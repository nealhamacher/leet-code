class Solution(object):
    # Runtime - 34 ms, beats 36.96%, Memory - 11.63MB, beats 52.60%
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        sum = 0
        while i < len(s):
            if s[i] == 'M':
                sum += 1000
            if s[i] == 'D':
                sum += 500
            if s[i] == 'C': 
                if (i < len(s) - 1) and (s[i+1] == 'M' or s[i+1] == 'D'):
                    sum -= 100
                else:
                    sum += 100
            if s[i] == 'L':
                sum += 50
            if s[i] == 'X':
                if (i < len(s) - 1) and (s[i+1] == 'C' or s[i+1] == 'L'):
                    sum -= 10
                else:
                    sum += 10
            if s[i] == 'V':
                sum += 5
            if s[i] == 'I':
                if (i < len(s) - 1) and (s[i+1] == 'X' or s[i+1] == 'V'):
                    sum -= 1
                else:
                    sum += 1
            i += 1
        return sum


################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))
    print(sol.romanToInt("LVIII"))
    print(sol.romanToInt("MCMXCIV"))
