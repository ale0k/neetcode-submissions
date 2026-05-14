class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip('-').isnumeric():
                stack.append(int(token))
            else:
                if token == "+":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    res = num1 + num2
                elif token == "-":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    res = num1 - num2
                elif token == "*":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    res = num1 * num2
                else:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    res = int(num1 / num2)
                stack.append(res)
            print(stack)
        return stack.pop()