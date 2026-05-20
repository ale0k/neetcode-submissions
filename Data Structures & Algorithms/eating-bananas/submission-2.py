class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_max_eat = 0
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / mid)
                
            if hours > h:
                l = mid + 1
            else:
                r = mid - 1
                min_max_eat = mid

                

        return min_max_eat