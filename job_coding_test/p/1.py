def solution(estimates, k):
    arr = []
    s = 0

    for i in range(len(estimates)):
        s += estimates[i]

        if i >= k - 1:
            arr.append(s)
            s -= estimates[i + 1 - k]

    return max(arr)