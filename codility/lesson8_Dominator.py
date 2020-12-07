def solution(A):
    if not len(A):
        return -1

    temp = list(A)
    temp.sort()
    candidate = temp[len(A) // 2]
    return A.index(candidate) if A.count(candidate) > len(A) / 2 else -1