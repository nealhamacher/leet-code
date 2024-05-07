# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        bfs_queue = [root]
        level_averages = []
        while(len(bfs_queue) > 0):
            current_level = len(bfs_queue)
            sum = 0
            for i in range(current_level):
                node = bfs_queue.pop(0)
                sum += node.val
                if node.left != None:
                    bfs_queue.append(node.left)
                if node.right != None:
                    bfs_queue.append(node.right)
            level_averages.append(float(sum)/current_level)
        return level_averages
        

################################################################################

if __name__ == "__main__":
    sol = Solution()
    n4 = TreeNode(7)
    n3 = TreeNode(15)
    n2 = TreeNode(20, n3, n4)
    n1 = TreeNode(9)
    n0 = TreeNode(3, n1, n2)
    print(sol.averageOfLevels(n0))
                    
                    