N, M = map(int, input().split())

s = []


def btrack():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return None

    for i in range(1, N + 1):
        if i in s:
            continue
        s.append(i)
        btrack()
        s.pop()


btrack()
