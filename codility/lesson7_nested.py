def solution(S):
    count = 0

    for ch in S:
        if ch == '(':
            count += 1
        else:
            if count < 1:
                return 0
            else:
                count -= 1
    
    if count > 0:
        return 0
    else:
        return 1