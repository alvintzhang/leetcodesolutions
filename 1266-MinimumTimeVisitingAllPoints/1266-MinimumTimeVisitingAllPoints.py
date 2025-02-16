class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time = 0
        if(len(points)==1):
            return time
        for i in range(len(points)-1):
            x = abs(points[i+1][0]-points[i][0])
            y = abs(points[i+1][1]-points[i][1])
            time+=max(x,y)

        return time