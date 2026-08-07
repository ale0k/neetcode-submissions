class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        freq_list = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for num, count in freq_map.items():
            freq_list[count].append(num)
        
        for i in range(len(freq_list) - 1, 0, -1):
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res