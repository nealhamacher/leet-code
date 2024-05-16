class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return ""
        
        letters = {2: ['a','b','c'], 
                   3:['d','e','f'],
                   4: ['g','h','i'],
                   5: ['j','k','l'],
                   6: ['m','n','o'],
                   7: ['p','q','r','s'],
                   8: ['t','u','v'],
                   9: ['w','x','y','z']}
        
        output = []
        for letter in letters[int(digits[0])]:
            print(letter)
            print(type(digits[1:]))
            string = letter + self.letterCombinations(digits[1:])

        return output.append(string)
        

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))