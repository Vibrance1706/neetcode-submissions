class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def add(a, b):
            return a+b
        
        def sub(a, b):
            return a-b
        
        def mul(a, b):
            return a*b

        def div(a, b):
            return a/b

        op_list = {'+': add, '-': sub, '*': mul, '/': div} 

        stack = []
        for token in tokens:
            if token in op_list:
                a = stack.pop()
                b = stack.pop()       
                val = op_list[token](b, a)         
                stack.append(int(val))
            else: 
                stack.append(int(token))
        
        return stack[-1]
