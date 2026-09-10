class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # while len(tokens) > 1:
        #     for i in range(len(tokens)):
        #         if tokens[i] in "+-/*":
        #             a = int(tokens[i-2])
        #             b = int(tokens[i-1])
        #             if tokens[i] == '+':
        #                 result = a + b
        #             elif tokens[i] == '-':
        #                 result = a - b
        #             elif tokens[i] == '*':
        #                 result = a * b
        #             elif tokens[i] == '/':
        #                 result = int(a / b)
        #             tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
        #             break
        # return int(tokens[0])

        stack = []
        for i in tokens:
            if i == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif i == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif i == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif i == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b / a)))
            else:
                stack.append(int(i))
        return stack[0]