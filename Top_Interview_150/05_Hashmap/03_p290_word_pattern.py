class Solution(object):
    # Runtime: 16 ms, beats 36.93%. Memory: 11.68 MB, beats 71.71%
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # Divide s into individual words
        split = s.split(" ")
        # Sanity check - same number of letters in pattern as words in s
        if len(split) != len(pattern):
            return False
        pattern_map = {}
        for i in range(len(pattern)):
            not_added = True
            for key, value in pattern_map.items():
                if (key == pattern[i] or value == split[i]):
                    if key != pattern[i] or value != split[i]:
                        return False
                    else:
                        not_added = False
            if not_added:
                pattern_map[pattern[i]] = split[i]

            
        # Reached end of pattern/words with no failure, is a match
        return True


################################################################################

if __name__ == "__main__":
    sol=Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))
    print(sol.wordPattern("abba", "dog cat cat fish"))
    print(sol.wordPattern("aaaa", "dog cat cat dog"))
    print(sol.wordPattern("aaaa", "dog cat cat dog"))