class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        longest = 0
        for num in set_of_nums:
            if num - 1 not in set_of_nums:
                length = 1
                while num + length in set_of_nums:
                    length += 1
                longest = max(longest, length)
        return longest