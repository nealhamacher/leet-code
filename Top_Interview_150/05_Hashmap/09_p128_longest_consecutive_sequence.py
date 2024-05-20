class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sequences = {}
        longest = 0
        for n in nums:
            if n in sequences:
                continue
            if (n-1) in sequences:
                # Both numbers above and below in hashmap
                if (n+1) in sequences:
                    current = sequences[n+1] + sequences[n-1] + 1
                    sequences[n+1+sequences[n+1]-1] = current # end of seq
                    sequences[n-1-sequences[n-1]+1] = current # beginning of seq
                    sequences[n] = current
                    if current > longest:
                        longest = current
                else:
                    current = sequences[n-1] + 1
                    sequences[n-1-sequences[n-1]+1] += 1
                    if current > longest:
                        longest = current
                    sequences[n] = current
            elif (n+1) in sequences:
                current = sequences[n+1] + 1
                sequences[n+1+(sequences[n+1])-1] += 1
                if current > longest:
                    longest = current
                sequences[n] = current
            else:
                sequences[n] = 1
                if 1 > longest:
                    longest = 1
        return longest


################################################################################
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(sol.longestConsecutive([1,2,0,1]))