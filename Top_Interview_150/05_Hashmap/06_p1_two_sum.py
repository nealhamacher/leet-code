class Solution(object):
    # Simple solution, O(n**2) time complexity
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    # Optimized solution using hashmap, O(n) time complexity
    def twoSum2(self, nums, target):
        difference_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in difference_map.keys():
                return [difference_map[diff], i]
            else:
                difference_map[nums[i]] = i
        return None

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
    print(sol.twoSum([3,2,4], 6))
    print(sol.twoSum([3,3], 6))
    
    print(sol.twoSum2([2,7,11,15], 9))
    print(sol.twoSum2([3,2,4], 6))
    print(sol.twoSum2([3,3], 6))