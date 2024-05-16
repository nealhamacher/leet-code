class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        combos = self.generateCombinations(digits, "")
        result = []
        for item in combos:
            result.extend(item)
        return result
        
    def generateCombinations(self, digits, output):
        """
        :type digits: str
        :type output: str
        :rtype: List[str]
        """
        
        if len(digits) == 0:
            return output
        
        letters = {'2': ['a','b','c'], 
                   '3':['d','e','f'],
                   '4': ['g','h','i'],
                   '5': ['j','k','l'],
                   '6': ['m','n','o'],
                   '7': ['p','q','r','s'],
                   '8': ['t','u','v'],
                   '9': ['w','x','y','z']}
        
        combinations = []

        for letter in letters[digits[0]]:
            combinations.append(self.generateCombinations(digits[1:], output+letter))
        return combinations


################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))