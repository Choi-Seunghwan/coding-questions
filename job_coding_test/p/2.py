def solution(office, k):
    result = 0
    N = len(office)

    for i in range(N - k + 1):
        for j in range(N - k + 1):
            count = 0
            for p1 in range(k):
                for p2 in range(k):
                    if office[p1 + i][p2 + j] == 1:
                        count += 1
            if count > result:
                result = count

    return result