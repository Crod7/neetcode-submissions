class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x,y in points:

            val = (x)**2 + (y)**2

            res.append([val,x,y,])

        heapq.heapify(res)

        result = []

        while k > 0:
            temp = heapq.heappop(res)
            result.append(temp[1:])
            k -= 1

        return result
            
