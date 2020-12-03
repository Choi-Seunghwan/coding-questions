def solution(X, A):
    # write your code in Python 3.6
    s = set()

    for i in range(0, len(A)):
        s.add(A[i])
        if len(s) >= X:
            return i
        
    return -1
