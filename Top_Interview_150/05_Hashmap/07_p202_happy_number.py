class Solution(object):
    # Using list
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
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
        return True
    
    # Using Floyd's tortoise and hare
    def isHappyFloyd(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def calculateNext(number):
            result = 0
            while number > 0:
                last_digit = number % 10
                result += last_digit * last_digit
                number = number // 10
            return result
        
        tortoise = calculateNext(n)
        print(tortoise)
        hare = calculateNext(calculateNext(n))
        while hare != 1:
            if tortoise == hare:
                return False
            else:
                tortoise = calculateNext(tortoise)
                print(tortoise)
                hare = calculateNext(calculateNext(hare))
        return True

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(19))
    print(sol.isHappyFloyd(19))
    print(sol.isHappy(2))
    print(sol.isHappyFloyd(2))