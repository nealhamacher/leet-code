class Solution(object):
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
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbb"))
    print(sol.lengthOfLongestSubstring("pwwkew"))
    
    
