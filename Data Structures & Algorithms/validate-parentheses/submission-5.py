class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            if char in ')}]':
                if not stack:
                    return False
                open_bracket = stack.pop()
                if open_bracket == '(' and char == ')' or open_bracket == '{' and char == '}' or open_bracket == '[' and char == ']':
                    continue
                else:
                    return False
        if stack:
            return False
        return True