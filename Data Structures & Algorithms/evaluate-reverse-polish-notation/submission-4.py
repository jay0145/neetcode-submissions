import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hset = {"+", "-", "*", "/"}
        stack = []

        for token in tokens:
            if token in hset and len(stack) > 1:
                second = int(stack.pop())
                first = int(stack.pop())
                #print(f"{first} {token} {second}")
                if token == "+":
                    
                    stack.append(first + second)

                elif token == "-":
                    stack.append(first - second)

                elif token == "*":
                    stack.append(first * second)

                elif token == "/":
                    stack.append(math.trunc(first / second))
                
                else:
                    return 0

            else:
                stack.append(token)
        
        return int(stack[-1])

                        
