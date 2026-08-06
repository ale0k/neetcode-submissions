class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            char = s[r]
            if char in char_set:
                while s[l] != char:
                    char_set.remove(s[l])
                    l += 1
                l += 1
            char_set.add(char)
            longest = max(longest, r-l+1)
        return longest