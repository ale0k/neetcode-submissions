class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        max_length = 0
        l = 0

        for r in range(len(s)):
            char = s[r]
            if char in mp:
                l = max(mp[char] + 1, l)
            mp[char] = r
            max_length = max(max_length, r - l + 1)
        return max_length