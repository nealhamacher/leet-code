# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return ["null"]
        elif len(nums) == 1:
            return [nums[0]]
        
        else:
            mid_idx = (len(nums)-1)//2
            bst = [nums[mid_idx]]
            bst += self.sortedArrayToBST(nums[0:mid_idx])
            bst += self.sortedArrayToBST(nums[mid_idx+1:len(nums)])
            return bst


################################################################################
if __name__ == "__main__":
    sol = Solution()
    print(sol.sortedArrayToBST([-10,-3,0,5,9]))
