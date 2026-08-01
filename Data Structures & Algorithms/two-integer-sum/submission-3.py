class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            hash_table[target - nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] in hash_table and i != hash_table[nums[i]]:
                return [i, hash_table[nums[i]]]
