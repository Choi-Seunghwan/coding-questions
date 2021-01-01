N, M = map(int, input().split())
arr = []


def solution(n):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, N + 1):
        arr.append(i)
        solution(i + 1)
        arr.pop()


solution(1)