class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter_map = {}
        for letter in s:
            if letter in letter_map.keys():
                letter_map[letter] += 1
            else:
                letter_map[letter] = 1
        for letter in t:
            if (letter not in letter_map.keys()) or letter_map[letter] == 0:
                return False
            else:
                letter_map[letter] -= 1
        return True
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))
    print(sol.isAnagram("rat", "car"))