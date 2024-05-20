class Solution(object):
    # Runtime: 368 ms, beats 53.08%. Memory: 32.67 MB, beats 9.89%
    # This version tracks all numbers
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        sequences = {}
        longest = 1
        for n in nums:
            if n in sequences:
                continue
            if (n-1) in sequences:
                # Both numbers above and below in hashmap
                if (n+1) in sequences:
                    current = sequences[n+1] + sequences[n-1] + 1
                    sequences[n+sequences[n+1]] = current # end of seq
                    sequences[n-sequences[n-1]] = current # beginning of seq
                    sequences[n] = current
                    if current > longest:
                        longest = current
                else:
                    current = sequences[n-1] + 1
                    sequences[n-current+1] += 1
                    if current > longest:
                        longest = current
                    sequences[n] = current
            elif (n+1) in sequences:
                current = sequences[n+1] + 1
                sequences[n+current-1] += 1
                if current > longest:
                    longest = current
                sequences[n] = current
            else:
                sequences[n] = 1
        return longest

    # This version tracks ends of sequences only
    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        ends = {}
        longest = 1

        for n in nums:
            if n in ends:
                continue
            if (n-1) in ends:
                # Both numbers above and below in hashmap
                if (n+1) in ends:
                    current = ends[n+1] + ends[n-1] + 1
                    ends[n+ends[n+1]] = current # end of seq
                    ends[n-ends[n-1]] = current # beginning of seq
                    if current != 3:
                        del ends[n+1]
                        del ends[n-1]
                    if current > longest:
                        longest = current
                else:
                    current = ends[n-1] + 1
                    ends[n-ends[n-1]] += 1
                    if current != 2:
                        del ends[n-1]
                    if current > longest:
                        longest = current
                    ends[n] = current
            elif (n+1) in ends:
                current = ends[n+1] + 1
                ends[n+ends[n+1]] += 1
                if current != 2:
                    del ends[n+1]
                if current > longest:
                    longest = current
                ends[n] = current

            else:
                ends[n] = 1
        return longest

################################################################################
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(sol.longestConsecutive([1,2,0,1]))
    print("\n")
    print(sol.longestConsecutive2([100,4,200,1,3,2]))
    print(sol.longestConsecutive2([0,3,7,2,5,8,4,6,0,1]))
    print(sol.longestConsecutive2([1,2,0,1]))