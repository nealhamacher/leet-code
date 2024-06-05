class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        order = {}
        for current in nums:
            n_larger = 0
            for compare in nums:
                if compare >= current:
                    n_larger += 1
            if n_larger == k:
                return current
            
            order[current] = n_larger

        closest_n = 0
        closest_dist = 9999
        for number in order.keys():
            if order[number] <  closest_dist and order[number] - k > 0:
                closest_n = number
                closest_dist = order[number]
        return closest_n
    
    def findKthLargestSorting(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return (sorted(nums, reverse = True)[k-1])
                         



sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))
print(sol.findKthLargest([3,2,1,5,6,4], 1))
print(sol.findKthLargest([99,99], 1))
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 20))