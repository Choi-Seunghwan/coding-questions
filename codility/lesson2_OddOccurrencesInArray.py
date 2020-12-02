def solution(A):
    A.sort()
    ASize = len(A)

    for i in range(0, ASize, 2):
        if (i + 1) >= ASize or A[i] != A[i + 1]:
            return A[i]

A = [1, 1, 3]

print(solution(A))
