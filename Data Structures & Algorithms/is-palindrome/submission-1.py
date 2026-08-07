class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = []
        for char in s:
            if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <='z') or (char.isdigit() and char in '0123456789'):
                lowered_char = char.lower()
                cleaned_string.append(lowered_char)
        l = 0
        r = len(cleaned_string) - 1
        while l <= r:
            if cleaned_string[l] != cleaned_string[r]:
                return False
            l += 1
            r -= 1
        return True