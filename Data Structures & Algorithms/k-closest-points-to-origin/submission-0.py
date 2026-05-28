import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_queue = []
        heapq.heapify(heap_queue)
        res = []
        for point in points:
            x, y = point
            distance = self.euclideanDistance((0, 0), (x, y))
            heapq.heappush(heap_queue, (distance, point))

        for i in range(k):
            distance, point = heapq.heappop(heap_queue)
            res.append(point)
        return res
        
        

    def euclideanDistance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)