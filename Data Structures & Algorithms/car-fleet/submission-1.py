class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        res = 0
        for i in range(len(speed)):
            pairs.append((position[i], speed[i]))
        sorted_pairs = sorted(pairs, reverse=True)

        for p, s in sorted_pairs:
            time = (target - p) / s
            if stack and stack[-1][1] >= time:
                continue
            stack.append((p, time))
            res += 1
        return res