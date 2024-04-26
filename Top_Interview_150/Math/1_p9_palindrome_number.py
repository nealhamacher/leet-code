class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        forward = str(x)
        reverse = forward[::-1]
        return(forward == reverse)
    
    def isPalindromeNoString(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        n_digits = 1
        values = []
        temp = x
        while temp//10 > 0:
            values.append(temp % 10)
            n_digits += 1
            temp = temp//10
        values.append(temp%10)
        i = 0
        j = n_digits-1
        while i < j:
            if values[i] != values[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

    
################################################################################

if __name__ == "__main__":
    sol = Solution()
    x = 121 
    print(sol.isPalindrome(x))
    print(sol.isPalindromeNoString(x))
    x = -121 
    print(sol.isPalindrome(x))
    print(sol.isPalindromeNoString(x))
    x = 10 
    print(sol.isPalindrome(x))
    print(sol.isPalindromeNoString(x))