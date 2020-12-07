def solution(A, B):
    opp = []
    resultCount = 0
    
    for i in range(len(A)):
        if B[i] == 1:
            opp.append(A[i])
            continue
        
        if len(opp) == 0:
            resultCount += 1
        else:
            while len(opp):
                oppFish = opp[-1]
                if oppFish > A[i]:
                    break
                else:
                    opp.pop()
            if len(opp) == 0:
                resultCount += 1
                
    return resultCount + len(opp)