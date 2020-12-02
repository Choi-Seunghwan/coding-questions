def solution(N):
    num: int = N
    bStr: str = ''
    maxGap: int = 0
    gap:int = 0

    while num > 0:
        bStr = str(num % 2) + bStr
        num //= 2

    for i in bStr:
        if i == '1':
            if maxGap < gap:
                maxGap = gap
            gap = 0
        else:
            gap += 1

    return maxGap

print(solution(529))