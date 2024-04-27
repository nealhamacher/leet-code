class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ret = [0]*len(digits)
        i = len(digits) - 1
        incremented = False
        while i >= 0:
            if incremented:
                ret[i] = digits[i]
            else:
                if digits[i] != 9:
                    ret[i] = digits[i]+1
                    incremented = True
                else:
                    ret[i] = 0
            i -= 1
        if not incremented:
            ret.insert(0, 1)
        return ret
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    digits = [1,2,3]
    print(sol.plusOne(digits))
    digits = [4,3,2,1]
    print(sol.plusOne(digits))
    digits = [9]
    print(sol.plusOne(digits))
    digits = [9,1,9]
    print(sol.plusOne(digits))
    digits = [9,9,9]
    print(sol.plusOne(digits))
    digits = [8,9,9]
    print(sol.plusOne(digits))
    
    