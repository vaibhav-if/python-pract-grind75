class Solution:
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+" or t == "-" or t == "*" or t == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                t = self.evaluate(t, num1, num2)
                stack.append(t)
            else:
                stack.append(int(t))

        return stack[0]

    def evaluate(self, op, num1, num2) -> int:
        return int(self.operators[op](num1, num2))
    
sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
