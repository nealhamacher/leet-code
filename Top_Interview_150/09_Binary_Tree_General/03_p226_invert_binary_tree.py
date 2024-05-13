# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    n6 = TreeNode(9)
    n5 = TreeNode(6)
    n4 = TreeNode(3)
    n3 = TreeNode(1)
    n2 = TreeNode(7, n5, n6)
    n1 = TreeNode(2, n3, n4)
    n0 = TreeNode(4, n1, n2)
    root = sol.invertTree(n0)
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.left.left.val)
    print(root.left.right.val)
    print(root.right.left.val)
    print(root.right.right.val)
