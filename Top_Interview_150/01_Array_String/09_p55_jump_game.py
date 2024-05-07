class Solution(object):
    # Inefficient solution - looks for zero or negative values, backtraces from
    # these points to see if we can jump over these points
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            if nums[i] <= 0:
                for j in range(1, i+1):
                    if nums[i-j] > j:
                        break
                    if j == i:
                        return False
        return True

    # More efficient solution - looks at how far we can go from each point,
    # stops when we hit last index
    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump = nums[0]
        for i in range(1, len(nums)-1):
            # Decrease maximum jump by one each iteration
            max_jump -= 1
            # If can jump further from current position than remaining jump,
            # then overweite max jump
            if nums[i] > max_jump:
                max_jump = nums[i]

            # If we can reach the last index, can jump
            if max_jump + i >= len(nums) - 1:
                return True
            # If we hit 0 jumps left, cannot make it
            if max_jump <= 0:
                return False
            
  
################################################################################
if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,1,1,4]
    print(sol.canJump(nums))
    print(sol.canJump2(nums))
    nums = [3,2,1,0,4]
    print(sol.canJump(nums))
    print(sol.canJump2(nums))