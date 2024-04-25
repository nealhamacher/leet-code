class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matches = {')':'(', '}':'{', ']':'['} # Matches close bracket to open
        stack = [] # Stack for holding brackets
        for char in s:
            if char in matches.values():
                stack.append(char)
            elif char in matches.keys():
                if len(stack) == 0: #Covers close bracket without open
                    return False
                current = stack.pop()
                if current != matches[char]:
                    return False
        if len(stack) != 0:
            return False
        return True
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    s = "()"
    print(str(sol.isValid(s)) + " (Should be True)")
    s = "()[]{ }"
    print(str(sol.isValid(s)) + " (Should be True)")
    s = "(]"
    print(str(sol.isValid(s)) + " (Should be False)")
    s = ")"
    print(str(sol.isValid(s)) + " (Should be False)")
    s = "a*(x(x+4(6)))"
    print(str(sol.isValid(s)) + " (Should be True)")
    s = "a*(x(x+4(6))"
    print(str(sol.isValid(s)) + " (Should be False)")