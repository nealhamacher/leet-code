class Solution(object):
    def rotate(self, nums, k): # Method 1 - pop and insert
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        rot = k % len(nums)
        print(rot)
        for i in range(0, rot):
            tmp =nums.pop()
            nums.insert(0, tmp)

    def rotate2(self, nums, k): # Method 2 - copy and replace
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        rot = k % len(nums)
        nums[0:len(nums)-rot+1], nums[len(nums)-rot+1:len(nums)] = nums[len(nums)-rot:len(nums)], nums[0:len(nums)-rot]

    
    def rotate3(self, nums, k): # Method 3 - consectutive rotations, in-place w/ O(1) extra space
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        rot = k % len(nums)
        for i in range(rot):
            print(i)
            next_in = nums[len(nums)-1]
            for j in range(len(nums)):
                current = nums[j]
                nums[j] = next_in
                next_in = current
            print(nums)
        

################################################################################

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5,6,7]
    sol.rotate(nums, 3)
    print(nums)
    nums = [1,2,3,4,5,6,7]
    sol.rotate2(nums, 3)
    print(nums)
    nums = [1,2,3,4,5,6,7]
    sol.rotate3(nums, 3)
    print(nums)
    