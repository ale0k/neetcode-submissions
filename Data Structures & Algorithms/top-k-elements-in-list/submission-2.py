class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        freq_list = []
        res = []

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for key, count in freq_map.items():
            freq_list.append((count, key))
        
        freq_list.sort(reverse=True)

        for i in range(k):
            res.append(freq_list[i][1])
        
        return res