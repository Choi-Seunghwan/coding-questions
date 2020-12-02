# codility lesson 4

A = [1]

def solution(A):
    # write your code in Python 3.6
    tempA = list(set(A))
    tempA.sort()
    maxNum = max(tempA)
    pIndex = 0
    
    if maxNum < 1:
        return 1
        
    for i in range(0, len(tempA)):
        if tempA[i] > 0:
            pIndex = i
            break
        
    tempA = tempA[pIndex:]
    
    for i in range(0, len(tempA)):
        if i + 1 != tempA[i]:
            return i + 1

    return maxNum + 1


print(solution(A))