class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            num = nums[i]

            if num in hash_map and hash_map[num] != i:
                return [hash_map[num], i]
            
            diff = target - num
            hash_map[diff] = i

        return []