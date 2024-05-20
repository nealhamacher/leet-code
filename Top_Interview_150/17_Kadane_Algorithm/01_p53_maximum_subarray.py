class Solution(object):
    # Runtime: 498 ms, beats 97.11%. Memory: 24.58 MB, beats 75.79%
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
        
        max_so_far = -2147483648 # Smallest 32-bit signed int, online submittal doesn't allow importing math
        max_ending_here = 0
        for num in nums:
            max_ending_here = max_ending_here + num
            if max_so_far < max_ending_here:
                max_so_far =  max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far