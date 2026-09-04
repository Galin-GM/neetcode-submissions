class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if len(tokens) == 1:
            return int(tokens[-1])

        ans = 0
        stack = []

        def is_operator(ch):
            return ch == '+' or ch == '-' or ch == '*' or ch == '/'


        for t in tokens:
            stack.append(t)

            if is_operator(t):
                # print(stack)
                op = stack[-1]
                stack.pop()
                num1 = int(stack[-1])
                stack.pop()
                num2 = int(stack[-1])
                stack.pop()

                if op == '+':
                    stack.append(num2 + num1)
                elif op == '-':
                    stack.append(num2 - num1)
                elif op == '*':
                    stack.append(num2 * num1)
                else :
                    a = num2 / num1
                    if a < 0:
                        a = math.ceil(a)
                    else:
                        a = math.floor(a)
                    stack.append(a)

        return stack[-1]
            