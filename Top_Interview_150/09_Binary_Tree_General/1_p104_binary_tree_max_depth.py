# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        

################################################################################

if __name__ == "__main__":
    sol = Solution()
    n4 = TreeNode(7)
    n3 = TreeNode(15)
    n2 = TreeNode(20, n3, n4)
    n1 = TreeNode(9)
    n0 = TreeNode(3, n1, n2)
    print(sol.maxDepth(n0))