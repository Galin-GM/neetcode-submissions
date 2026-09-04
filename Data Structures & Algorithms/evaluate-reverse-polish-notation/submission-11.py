class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if len(tokens) == 1:
            return int(tokens[-1])

        stack = []

        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                a = num2 / num1
                if a < 0:
                    a = math.ceil(a)
                else:
                    a = math.floor(a)
                stack.append(a)
            else:
                stack.append(int(t))

        return stack[-1]
            