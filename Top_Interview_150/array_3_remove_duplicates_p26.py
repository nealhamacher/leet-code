class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        n_unique = len(nums)
        while j < len(nums):
            if nums[i] == nums[j]:
                nums[j] = "_"
                j += 1
                n_unique -= 1
            else:
                i = j
                j += 1
        return n_unique

################################################################################

if __name__ == "__main__":
    s = Solution()

    nums = [1,1,2]
    print(s.removeDuplicates(nums))
    print(nums)

    nums = [0,0,1,1,1,2,2,3,3,4]
    print(s.removeDuplicates(nums))
    print(nums)
    
    nums = []
    print(s.removeDuplicates(nums))
    print(nums)

    nums = [0]
    print(s.removeDuplicates(nums))
    print(nums)

