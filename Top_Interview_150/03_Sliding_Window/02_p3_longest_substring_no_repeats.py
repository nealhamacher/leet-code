class Solution(object):
    # Runtime: 182 ms, beats 21.90%. Memory: 12.59 MB, beats 32.76%
    # Uses copy of substring
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        else:
            substring = s[0]
            longest = length = 1
        for i in range(1, len(s)):
            for j in range(len(substring)-1, -1, -1):
                if s[i] == substring[j]:
                    if length > longest:
                        longest = length
                    substring = substring[j+1:] + s[i]
                    length = len(substring)
                    break
            else:
                substring += s[i]
                length += 1
        if length > longest:
            return length
        return longest
    
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        else:
            start = 0
            end = 0
            longest = 1
        for i in range(1, len(s)):
            for j in range(end, start-1, -1):
                if end - start + 1 > longest:
                    longest = end - start + 1
                if s[i] == s[j]:
                    start = j+1
                    end = i
                    break
            else:
                end += 1
        return longest

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbb"))
    print(sol.lengthOfLongestSubstring("pwwkew"))
    print("\n")
    print(sol.lengthOfLongestSubstring2("abcabcbb"))
    print(sol.lengthOfLongestSubstring2("bbbbb"))
    print(sol.lengthOfLongestSubstring2("pwwkew"))
    
    
