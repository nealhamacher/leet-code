class Solution(object):
    # Runtime: 17ms, beats 25.47%. Memory: 11.91 MB, beats 24.95%
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        last_word_length = 0
        while s[i] != ' ' and i >= 0:
            i -= 1
            last_word_length += 1
        return last_word_length
    
    def lengthOfLastWord2(self, s):
        # Runtime: 17ms, beats 57.66% . Memory: 11.86 MB, beats 55.62%
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        if not words:
            return 0
        else:
            return len(words[-1])