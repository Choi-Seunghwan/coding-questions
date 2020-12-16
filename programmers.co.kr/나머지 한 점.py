def solution(v):
    tempX = []
    tempY = []

    for pos in v:
        x = pos[0]
        y = pos[1]

        if x in tempX:
            tempX.remove(x)
        else:
            tempX.append(x)

        if y in tempY:
            tempY.remove(y)
        else:
            tempY.append(y)

    return [tempX[0], tempY[0]]