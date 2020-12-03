def solution(A):
    # write your code in Python 3.6
    A.sort()
    flag = 1

    for i in range(len(A)):
        if i + 1 != A[i]:
            flag = 0
            break
    
    return flag
