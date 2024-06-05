class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        if nums[(len(nums)+1)//2] == nums[0]:
            return nums[0]
        else:
            return nums[len(nums)//2]

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime 164ms, beats 43.48%. Memory 14.02Mb, beats 7.89%
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
    print(sol.majorityElement([3,2,3]))
    print(sol.majorityElement([2,2,1,1,1,2,2]))
    print(sol.majorityElement([6,5,5]))
    print(sol.majorityElement([2,2]))