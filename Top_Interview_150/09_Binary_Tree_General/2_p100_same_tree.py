class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Base Case - No node in both trees at current position
        if p == None and q == None:
            return True
        
        else:
            # False case - No node in one tree but is node in other
            if p == None or q == None:
                return False
            # False case - node values are not same
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

################################################################################
if __name__ == "__main__":
    sol = Solution()
    p2 = TreeNode(3)
    p1 = TreeNode(2)
    p0 = TreeNode(0, p1, p2)
    q2 = TreeNode(3)
    q1 = TreeNode(2)
    q0 = TreeNode(0, q1, q2)
    print(sol.isSameTree(p0,q0))
    p0 = TreeNode(1, p1)
    q0 = TreeNode(1, None, q1)
    print(sol.isSameTree(p0,q0))