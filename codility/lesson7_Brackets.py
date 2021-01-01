def solution(S):
    stack = []

    for ch in S:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        else: # ], }, )
            if len(stack) < 1:
                return 0
            item = stack.pop()
            if ch == ']' and item != '[':
                return 0
            elif ch == '}' and item != '{':
                return 0
            elif ch == ')' and item != '(':
                return 0
    
    if len(stack) > 0:
        return 0
    else:
        return 1