class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = {}
        for char in magazine:
            if char not in letters.keys():
                letters[char] = 1
            else:
                letters[char] += 1
        for char in ransomNote:
            if char not in letters.keys():
                return False
            elif letters[char] == 0:
                return False
            else:
                letters[char] -= 1
        return True


################################################################################

if __name__ == "__main__":
    sol = Solution()
    ransomNote = "a" 
    magazine = "b"
    print(sol.canConstruct(ransomNote, magazine))
    ransomNote = "aa" 
    magazine = "ab"
    print(sol.canConstruct(ransomNote, magazine))
    ransomNote = "aa" 
    magazine = "aab"
    print(sol.canConstruct(ransomNote, magazine))