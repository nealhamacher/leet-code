# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        else:
            mid_idx = (len(nums)-1)//2
            return TreeNode(
                nums[mid_idx],
                self.sortedArrayToBST(nums[0:mid_idx]),
                self.sortedArrayToBST(nums[mid_idx+1:len(nums)])
            )
            

################################################################################
if __name__ == "__main__":
    sol = Solution()
    root = sol.sortedArrayToBST([-10,-3,0,5,9])
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.left.left)
    print(root.left.right.val)
    print(root.right.left)
    print(root.right.right.val)
