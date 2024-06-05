class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stripped = ""
        for char in s:
            if char.isspace():
                continue
            elif char.isalpha():
                stripped += char.lower()
            else:
                stripped += char

        for i in range((len(stripped)+1)//2):
            if stripped[i] != stripped[len(stripped)-1-i]:
                return False
        return True

    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            while not s[i].isalnum():
                i += 1
                if i > j:
                    return True
            while not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
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
    