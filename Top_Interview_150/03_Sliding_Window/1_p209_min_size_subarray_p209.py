class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        size = 1
        while size < len(nums):
            i = 0 
            while i < len(nums) - size + 1:
                if sum(nums[i:i+size]) >= target:
                    return size
                i += 1
            size += 1
        return 0
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    t = 7
    ns = [2,3,1,2,4,3]
    print(sol.minSubArrayLen(t, ns))
    t = 4
    ns = [1,4,4]
    print(sol.minSubArrayLen(t, ns))
    t = 11
    ns = [1,1,1,1,1,1,1,1]
    print(sol.minSubArrayLen(t, ns))