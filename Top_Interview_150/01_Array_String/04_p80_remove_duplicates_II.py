class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Remove duplicates step
        k = len(nums)
        n_dups = 1
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+n_dups]:
                if n_dups != 1:
                    nums[i+n_dups] = "_"
                    k -= 1
                n_dups += 1
            else:
                i = i + n_dups
                n_dups = 1

        last_idx = len(nums)-1
        i = 0
        while i < last_idx:
            if nums[i] == "_":
                j = i
                while j < last_idx:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    j += 1
                last_idx -= 1
            else:
                i += 1
        return k        

################################################################################

if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,2,2,3]
    print(sol.removeDuplicates(nums))
    print(nums)

