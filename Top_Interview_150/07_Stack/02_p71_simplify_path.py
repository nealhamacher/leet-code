class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for i in range(len(path)):
            current = ''
            if path[i] == '.':
                if i == len(path) or path[i+1] == '/':
                    continue
                elif path[i+1] == '.':
                    if len(stack) == 0:
                        continue
                    if i+1 == len(path) or path[i+2] == '/':
                        stack.pop(len(stack)-1)
                    else:
                        while i < len(path)-1 and path[i] != '/':
                            current += path[i]
                            i += 1
            elif path[i] == '/':
                stack.append('/')
                while i < len(path)-1 and path[i+1] == '/':
                        i += 1
            else:
                while i < len(path)-1 and path[i+1] != '/':
                        current += path[i]
                        i += 1
            if current != '':
                 stack.append(current)
        if stack[len(stack)-1] == '/':
            stack.pop(len(stack)-1)
        if len(stack) == 0:
            stack=["/"]
        print(stack)


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
                