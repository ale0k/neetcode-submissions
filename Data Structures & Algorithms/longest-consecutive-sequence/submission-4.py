class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        longest_sequence = 0
        current_sequence = 0
        previous_num = None
        for num in sorted_nums:
            if previous_num == None or num == previous_num + 1:
                current_sequence += 1
            elif num == previous_num:
                continue
            else:
                longest_sequence = max(longest_sequence, current_sequence)
                current_sequence = 1
            previous_num = num
        return max(longest_sequence, current_sequence)