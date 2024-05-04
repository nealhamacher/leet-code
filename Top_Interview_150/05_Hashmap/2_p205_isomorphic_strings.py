class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map = {}
        t_map = {}
        if len(s) != len(t): # Sanity check - ensure same size strings
            return False
        
        for i in range(len(s)): # Iterate through each character

            # First time seeing a character in s
            if s[i] not in s_map.keys(): 
                # Not first time seeing corresponding character in t -> not iso
                if t[i] in t_map.keys():
                    return False
                # First time seeing char in both: add to hashmaps
                else:
                    s_map[s[i]] = [i]
                    t_map[t[i]] = [i]
            
            # Not first time seeing character in s
            else: 
                # First time seeing character in t -> not iso
                if t[i] not in t_map.keys(): 
                    return False
                else:
                    # Ensure previous corresponding characters at same indices
                    if s_map[s[i]] != t_map[t[i]]:
                        return False
                    else:
                        s_map[s[i]].append(i)
                        t_map[t[i]].append(i)
        return True
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.isIsomorphic("egg", "add"))
    print(sol.isIsomorphic("foo", "bar"))
    print(sol.isIsomorphic("paper", "title"))