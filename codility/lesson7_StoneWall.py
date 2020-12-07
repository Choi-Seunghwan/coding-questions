def solution(H):
    stack = []
    count = 0

    for block in H:
        if len(stack) == 0:
            stack.append(block)
            count += 1
        else:
            while len(stack):
                if stack[-1] > block:
                    stack.pop()
                else:
                    break
            if len(stack) == 0 or stack[-1] < block:
                stack.append(block)
                count += 1
    return count