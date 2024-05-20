import math

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        eqns = {}
        for p1 in range(len(points)):
            for p2 in range(p1+1, len(points)):
                if points[p2][0] == points[p1][0]:
                    m = math.inf
                else:
                    m = (points[p2][1]-points[p1][1]) / (points[p2][0]-points[p1][0])
                    b = points[p2][1] - (m*points[p2][0])
            if m == math.inf:
                b = points[p2][0]
            if (m, b) in eqns:
                eqns[(m,b)] += 1
            else:
                eqns[(m,b)] = 1
        
        max = 0
        for num in eqns.values():
            if num > max:
                max = num
        
        return max
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    points = [[1,1],[2,2],[3,3]]
    print(sol.maxPoints(points))
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(sol.maxPoints(points))
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4],[5,0],[0,5]]
    print(sol.maxPoints(points))
    points = [[1,1],[3,2],[5,3],[4,1],[4,2],[4,3],[4,4],[4,5]]
    print(sol.maxPoints(points))