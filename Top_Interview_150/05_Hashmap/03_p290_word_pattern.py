class Solution(object):
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
            # If pattern is in keys, has been matched with word already
            if pattern[i] in pattern_map.keys():
                # If current word is not already matched word, not a match
                if split[i] != pattern_map[pattern[i]]:
                    return False
            # If pattern not in map, add it and associate with corresponding word
            else:
                pattern_map[pattern[i]] = split[i]
        # Reached end of pattern/words with no failure, is a match
        return True


################################################################################

if __name__ == "__main__":
    sol=Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))
    print(sol.wordPattern("abba", "dog cat cat fish"))
    print(sol.wordPattern("aaaa", "dog cat cat dog"))