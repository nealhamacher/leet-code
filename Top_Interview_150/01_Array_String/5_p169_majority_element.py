class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = nums[0]
        count = 1
        start = 1
        while start < len(nums):
            for i in range(start, len(nums)):
                if nums[i] == current:
                    count += 1
                if count > len(nums) // 2:
                    return current
            start += 1
        return None

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurrences = {}
        for i in range(len(nums)):
            if nums[i] not in occurrences.keys():
                occurrences[nums[i]] = 1
            else:
                occurrences[nums[i]] += 1
            if occurrences[nums[i]] > len(nums) // 2:
                return nums[i]
        return None


            
################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement2([3,2,3]))
    print(sol.majorityElement2([2,2,1,1,1,2,2]))