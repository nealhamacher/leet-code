class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if (i+1) >= citations[i]:
                return i+1
        return 0


################################################################################

if __name__ == "__main__":
    sol = Solution()
    citations = [3,0,6,1,5]
    print(sol.hIndex(citations))
    citations = [1,3,1]
    print(sol.hIndex(citations))
    print(sol.hIndex([100]))