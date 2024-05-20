class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        for number in enumerate(nums):
            if number[1] in hashmap:
                if number[0] - hashmap[number[1]] <= k:
                    return True
                else:
                    hashmap[number[1]] = number[0]
            else:
                hashmap[number[1]] = number[0]
        return False
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2,3,1], 3))
    print(sol.containsNearbyDuplicate([1,0,1,1], 1))
    print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))