class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Runtime: 33 ms, beats 25.10%. Memory: 12.26 MB, beats 88.27% 
        def searchHelper(nums, start, end, target):
            if target > nums[end]:
                return end + 1
            if target < nums[start]:
                return start

            mid = (end + start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return searchHelper(nums, start, mid - 1, target)
            else:
                return searchHelper(nums, mid+1, end, target)
        
        start = 0
        end = len(nums) - 1
        return searchHelper(nums, start, end, target)
    

        

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 5))
    print(sol.searchInsert([1,3,5,6], 2))
    print(sol.searchInsert([1,3,5,6], 7))
    print(sol.searchInsert([1,3,5,6], 0))
    print(sol.searchInsert([1,3], 0))
    print(sol.searchInsert([1,3,5,6], 7))

