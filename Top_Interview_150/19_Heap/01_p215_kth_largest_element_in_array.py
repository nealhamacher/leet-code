class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for current in nums:
            n_larger = 0
            for compare in nums:
                if compare >= current:
                    n_larger += 1
            if n_larger == k:
                return current
            heap.append(n_larger)

        closest = 999999
        closest_idx = -1
        for i in range(len(heap)):
            if heap[i] - k > 0 and heap[i] - k < closest:
                closest_idx = i
                closest = heap[i] - k

        return nums[closest_idx]

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))
print(sol.findKthLargest([3,2,1,5,6,4], 1))
print(sol.findKthLargest([99,99], 1))
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 20))