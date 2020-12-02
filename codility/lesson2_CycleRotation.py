def solution(A, K):
    if len(A) < 1:
        return A

    q = list(A)
    
    for i in range(K):
        item = q.pop()
        q.insert(0, item)

    return q
    


A = [3, 8, 9, 7, 6]
K = 3

print(solution(A, K))