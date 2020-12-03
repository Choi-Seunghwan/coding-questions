def solution(A):
    A.sort()

    s1 = A[0] * A[1] * A[-1]
    s2 = A[-1] * A[-2] * A[-3]
    
    return s1 if s1 > s2 else s2