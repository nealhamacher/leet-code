# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        bfs_queue = [root]
        right_view = []
        while(len(bfs_queue) > 0):
            right_view.append(bfs_queue[-1].val)
            current_level = []
            for node in bfs_queue:
                if node.left != None:
                    current_level.append(node.left)
                if node.right != None:
                    current_level.append(node.right)
            bfs_queue = current_level
        return right_view
    
    def rightSideView2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        bfs_queue = [root]
        right_view = []
        while(len(bfs_queue) > 0):
            right_view.append(bfs_queue[-1].val)
            current_level = len(bfs_queue)
            for i in range(current_level):
                node = bfs_queue.pop(0)
                if node.left != None:
                    bfs_queue.append(node.left)
                if node.right != None:
                    bfs_queue.append(node.right)
        return right_view

################################################################################

if __name__ == "__main__":
    sol = Solution()
    n5 = TreeNode(7)
    n4 = TreeNode(4)
    n3 = TreeNode(5, n5)
    n2 = TreeNode(3, None, n4)
    n1 = TreeNode(2, None, n3)
    n0 = TreeNode(1, n1, n2)
    print(sol.rightSideView(n0))
    print(sol.rightSideView2(n0))
                    
                    


