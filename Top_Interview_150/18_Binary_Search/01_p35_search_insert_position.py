class Solution(object):
    # Recursive Solution
    # After optimizing - Runtime: 27 ms, beats 74.83%. Memory: 12.48 MB, beats 23.51% 
    # Original - Runtime: 33 ms, beats 25.10%. Memory: 12.26 MB, beats 88.27% 
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def searchHelper(nums, start, end, target, movedStart):
            if not movedStart and target > nums[end]:
                return end + 1
            if movedStart and target < nums[start]:
                return start

            mid = (end + start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return searchHelper(nums, start, mid - 1, target, False)
            else:
                return searchHelper(nums, mid+1, end, target, True)
        
        start = 0
        end = len(nums) - 1
        if nums[end] < target:
            return end + 1
        if nums[start] > target:
            return start
        return searchHelper(nums, start, end, target, False)
    

    # Iterative Solution
    # Runtime: 35 ms, beats 15.41%. Memory: 12.36 MB, beats 59.51% 
    def searchInsert2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1 
        mid = (end + start) // 2
        while nums[mid] != target:
            if target < nums[start]:
                return start
            elif target > nums[end]:
                return end + 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
            mid = (end + start) // 2
        return mid
        

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 5))
    print(sol.searchInsert([1,3,5,6], 2))
    print(sol.searchInsert([1,3,5,6], 7))
    print(sol.searchInsert([1,3,5,6], 0))
    print(sol.searchInsert([1,3], 0))
    print(sol.searchInsert([1,3,5,6], 7))
    print("\n")
    print(sol.searchInsert2([1,3,5,6], 5))
    print(sol.searchInsert2([1,3,5,6], 2))
    print(sol.searchInsert2([1,3,5,6], 7))
    print(sol.searchInsert2([1,3,5,6], 0))
    print(sol.searchInsert2([1,3], 0))
    print(sol.searchInsert2([1,3,5,6], 7))

