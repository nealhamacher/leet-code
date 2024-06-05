class Solution(object):
    # Runtime: 66 ms, beats 9.12%. Memory: 11.86 MB, beats 97.77%
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter_map = {}
        # Validity check - must be same word lengths
        if len(s) != len(t):
            return False
        for letter in s:
            # Letter already seen in s, increment number of occurences
            if letter in letter_map.keys():
                letter_map[letter] += 1
            # Otherwise add letter to map
            else:
                letter_map[letter] = 1
        for letter in t:
            # Letter is not in s, or occurs more times in t than in s
            if (letter not in letter_map.keys()) or letter_map[letter] == 0:
                return False
            # Otherwise decrement number of remaining allowed occurences of letter
            else:
                letter_map[letter] -= 1
        # Made it to end of t and all letters occured in s, so have an anagram
        return True
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))
    print(sol.isAnagram("rat", "car"))