class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Methodology - use time-space tradeoff to make arrays of indices in 
        # final nums1, use that to merge the arrays together
        i1 = 0
        i2 = 0
        idxs1 = []
        idxs2 = []
        # O(m+n)
        while (i1+i2) < (m+n):
            if nums1[i1] <= nums2[i2] and i1 < m:
               idxs1.append(i1+i2)
               i1 += 1
            else: 
                idxs2.append(i1+i2)
                i2 += 1
        # O(m)
        for i in range(len(idxs1)):
            nums1[idxs1[i]] = nums1[i]
        # O(n)
        for i in range(len(idxs2)):
            nums1[idxs2[i]] = nums2[i]



        

###############################################################################

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3
    s = Solution()
    s.merge(nums1, m, nums2, n)
    print(nums1)