class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while left < right and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                print(s[left], s[right])
                return False
            left += 1
            right -= 1
        return True
    
    def alphaNum(self, char):
        return (
            (ord('A') <= ord(char) and ord('Z') >= ord(char)) or
            (ord('a') <= ord(char) and ord('z') >= ord(char)) or
            (ord('0') <= ord(char) and ord('9') >= ord(char))
        )