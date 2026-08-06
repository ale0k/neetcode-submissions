class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_eat_per_hour = 1000000000
        l = 1
        r = max(piles)
        while l <= r:
            eat_rate = (l + r) // 2
            eats = 0
            for pile in piles:
                eats += math.ceil(pile / eat_rate)
                if eats > h:
                    break
            if eats > h:
                l = eat_rate + 1
            else:
                r = eat_rate - 1
                min_eat_per_hour = min(min_eat_per_hour, eat_rate)
        return min_eat_per_hour