class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stripped = ""
        for char in s:
            if char.isalpha():
                stripped += char.lower()

        for i in range((len(stripped)+1)//2):
            if stripped[i] != stripped[len(stripped)-1-i]:
                return False
        return True


################################################################################

if __name__ == "__main__":
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    print(sol.isPalindrome(s))
    s = "race a car"
    print(sol.isPalindrome(s))
    s = " "
    print(sol.isPalindrome(s))
    