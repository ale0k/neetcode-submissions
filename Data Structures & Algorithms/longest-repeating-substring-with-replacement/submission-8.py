class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        longest = 0

        l = 0
        max_freq = 0
        for r in range(len(s)):
            char = s[r]
            counts[char] = counts.get(char, 0) + 1
            max_freq = max(max_freq, counts[char])
            while r - l + 1 - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest