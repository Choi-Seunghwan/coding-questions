def solution(n):
    ball = n
    basket = 0

    while ball > 0:
        tempBall1 = ball
        tempBall2 = ball

        tempVal1 = int(ball ** 0.5)
        tempVal2 = tempVal1 - 1
        basket += 1

        for i in range(2):
            tempBall1 -= tempVal1 ** 2
            tempBall2 -= tempVal2 ** 2

            if tempBall1 == 0 or tempBall2 == 0:
                break

            if i == 0:
                tempVal1 = int(tempBall1 ** 0.5)
                tempVal2 = int(tempBall2 ** 0.5)
                basket += 1

        ball = min(tempBall1, tempBall2)

    return basket