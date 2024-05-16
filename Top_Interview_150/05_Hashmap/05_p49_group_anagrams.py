class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Determines if two strings have the same letters
        def compareStrings(current, string):
            if len(current) != len(string):
                return False
            # If a letter in string is found in current, remove from current 
            for i in range(len(string)):
                for j in range(len(current)):
                    if string[i] == current[j]:
                        current = current[:j] + current[j+1:]
                        break
            # At end, if current is empty string then we have an anagram
            if current == '':
                return True
            else:
                return False
        
        anagrams = []
        for string in strs:
            is_anagram = False
            for i in range(len(anagrams)):
                current = anagrams[i][0]
                is_anagram = compareStrings(current, string)
                if is_anagram:
                    anagrams[i].append(string)
                    break
            if not is_anagram:
                anagrams.append([string])
        return anagrams



################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))