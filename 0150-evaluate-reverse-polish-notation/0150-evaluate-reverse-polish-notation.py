class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '-':
                sub = stack.pop()
                target = stack.pop()
                stack.append(target - sub)
            elif token == '/':
                mod = stack.pop()
                target = stack.pop()
                stack.append(int(target / mod))
            else:
                stack.append(int(token))
            
        return stack.pop()