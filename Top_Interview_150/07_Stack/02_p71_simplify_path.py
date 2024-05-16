class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        elements = path.split('/')
        stack = []
        for element in elements:
            # Empty element (multiple consecutive /) or single period - ignored in output
            if element == '' or element == '.':
                continue
            # Two periods - navigate up one level, if stack is not empty
            elif element == '..':
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(element)

        # Empty stack - no path, have navigated to root
        if len(stack) == 0:
            return "/"
        
        output = ""
        for item in stack:
            output += "/"
            output += item
        
        return output


################################################################################

if __name__ == "__main__":
     sol = Solution()
     path = "/home//foo/"
     print(sol.simplifyPath(path))
     
     path = "/home/user/Documents/../Pictures"
     print(sol.simplifyPath(path))

     path = "/../"
     print(sol.simplifyPath(path))

     path = "/.../a/../b/c/../d/./"
     print(sol.simplifyPath(path))
                