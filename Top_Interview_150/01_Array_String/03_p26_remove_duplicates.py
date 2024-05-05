class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Remove duplicates step
        i = 0
        j = 1
        k = len(nums)
        while j < len(nums):
            if nums[i] == nums[j]:
                nums[j] = "_"
                j += 1
                k -= 1
            else:
                i = j
                j += 1
        

        #Bubble empty indices to end step
        last_idx = len(nums) - 1
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

