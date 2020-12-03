import sys

def solution(A):
    # write your code in Python 3.6
    minVal = sys.maxsize
    sumVal = sum(A)
    addVal = 0

    for i in range(0, len(A) - 1):
        addVal += A[i]
        sumVal -= A[i]
        absVal = abs(addVal - sumVal)

        if absVal < minVal:
            minVal = absVal
    
    return minVal