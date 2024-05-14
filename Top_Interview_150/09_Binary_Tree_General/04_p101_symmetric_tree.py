# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def compareTrees(self, left, right):
            if left == None and right == None:
                return True
            if (left == None and right != None) or (left != None and right == None):
                return False
            return (left.val == right.val and  
                    compareTrees(self, left.right, right.left) and 
                    compareTrees(self, left.left, right.right))
        
        return compareTrees(self, root.left, root.right)

################################################################################

if __name__ == "__main__":
    sol = Solution()
    n6 = TreeNode(3)
    n5 = TreeNode(4)
    n4 = TreeNode(4)
    n3 = TreeNode(3)
    n2 = TreeNode(2, n5, n6)
    n1 = TreeNode(2, n3, n4)
    n0 = TreeNode(1, n1, n2)
    print(sol.isSymmetric(n0))
    n4 = TreeNode(3)
    n3 = TreeNode(3)
    n2 = TreeNode(2, None, n4)
    n1 = TreeNode(2, None, n3)
    n0 = TreeNode(1, n1, n2)
    print(sol.isSymmetric(n0))

            