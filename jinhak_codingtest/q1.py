def solution(n):
    arr = list(str(n))
    
    while len(arr) > 1:
        sum = 0
        for i in arr:
            sum += int(i)
        arr = list(str(sum))
    
    return int(arr[0])