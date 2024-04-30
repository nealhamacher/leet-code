class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # Handle empty list
        if len(nums) == 0:
            return []
        else:
            results = []
            idx1 = 0
            i = 1
            while i < len(nums):
                if nums[i] != nums[idx1] + i - idx1:
                    idx2 = i-1
                    s = str(nums[idx1])
                    if idx2 != idx1:
                        s += ("->" + str(nums[idx2]))
                    results.append(s)
                    idx1 = i
                else:
                    i += 1
            s = str(nums[idx1])
            if idx1 != len(nums)-1:
                s += ("->" + str(nums[len(nums)-1]))
            results.append(s)
    
        return results
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,2,4,5,7]
    print(sol.summaryRanges(nums))
    nums = [0,2,3,4,6,8,9]
    print(sol.summaryRanges(nums))

        