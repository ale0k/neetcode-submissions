class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            # odd
            l, r = i, i
            res = self.expandCheck(s, res, l, r)

            # even
            l, r = i, i + 1
            res = self.expandCheck(s, res, l, r)

        return res

    def expandCheck(self, s, res, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r + 1]
            l -= 1
            r += 1
        return res
