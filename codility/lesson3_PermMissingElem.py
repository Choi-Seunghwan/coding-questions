def solution(A):
    # write your code in Python 3.6
    if len(A) < 1:
        return 1
        
    A.sort()
    count = 1

    for i in A:
        if i != count:
            return count
        count += 1

    return count