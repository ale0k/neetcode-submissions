class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        l = 0
        max_substring = 0
        max_freq = 0
        for r in range(len(s)):
            char = s[r]
            mp[char] = mp.get(char, 0) + 1
            max_freq = max(max_freq, mp[char])

            if r - l + 1 - max_freq > k:
                mp[s[l]] -= 1
                l += 1
            max_substring = max(max_substring, r - l + 1)
        return max_substring
            