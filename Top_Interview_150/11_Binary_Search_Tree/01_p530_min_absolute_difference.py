import math

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Base Case - No node, no abs difference (model this as infinity)
        if root == None:
            return math.inf

        else:
            # If no left child, then no nodes on left to find difference from root
            if root.left == None:
                val_left = -math.inf
            # Otherwise, smallest absolute diff will be between root and rightmost descendent of left child
            else:
                current = root.left
                val_left = current.val
                while current.right != None:
                    current = current.right
                    val_left = current.val

            # If no right child, then no nodes on right to find difference from root
            if root.right == None:
                val_right = math.inf
            # Otherwise, smallest absolute diff will be between root and rightmost descendent of left child
            else:
                current = root.right
                val_right = current.val
                while current.left != None:
                    current = current.left
                    val_right = current.val
            diff_left = root.val - val_left
            diff_right = val_right - root.val

            # Smallest absolute difference in tree will either be on left side, right side, or between two descendents
            return min(diff_left, 
                       diff_right, 
                       self.getMinimumDifference(root.left), 
                       self.getMinimumDifference(root.right))
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    n4 = TreeNode(4)
    n3 = TreeNode(1)
    n2 = TreeNode(12)
    n1 = TreeNode(2, n3, n4)
    n0 = TreeNode(8, n1, n2)
    print(sol.getMinimumDifference(n0))
            