class Solution(object):
    # Runtime - 14 ms, beats 75.30%. Memory - 11.64 MB, beats 35.85%
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i] == val:
                nums[i] = "_"
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return i


###############################################################################

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 2
    s = Solution()
    print(s.removeElement(nums, val))
    print(nums)