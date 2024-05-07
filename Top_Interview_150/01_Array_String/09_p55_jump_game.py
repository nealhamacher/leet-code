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
        max_end = nums[0]
        for i in range(1, len(nums)-1):
            max_end -= 1
            if nums[i] > max_end:
                max_end = nums[i]
            if max_end == 0:
                return False
        return True
            
  
################################################################################
if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,1,1,4]
    print(sol.canJump(nums))
    print(sol.canJump2(nums))
    nums = [3,2,1,0,4]
    print(sol.canJump(nums))
    print(sol.canJump2(nums))