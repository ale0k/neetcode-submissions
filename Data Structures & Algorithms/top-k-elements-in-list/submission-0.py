class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1
        list_of_items = list(freq_map.items())
        sorted_freq_map = sorted(list_of_items, key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_freq_map[i][0])
        return result