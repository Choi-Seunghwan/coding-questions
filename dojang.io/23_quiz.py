# https://dojang.io/mod/quiz/review.php?attempt=465075&cmid=2298
# 표준 입력으로 2차원 리스트의 가로(col)와 세로(row)가 입력되고 그 다음 줄부터 리스트의 요소로 들어갈 문자가 입력됩니다. 이때 2차원 리스트 안에서 *는 지뢰이고 .은 지뢰가 아닙니다. 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
#
# 여러 줄을 입력 받으려면 다음과 같이 for 반복문에서 input을 호출한 뒤 append로 각 줄을 추가하면 됩니다(list 안에 문자열을 넣으면 문자열이 문자 리스트로 변환됩니다).
#
# matrix = []
# for i in range(row):
#     matrix.append(list(input()))
# 이 문제는 지금까지 심사문제 중에서 가장 어렵습니다. 처음 풀어보는 경우 대략 두 시간은 걸립니다. 시간을 두고 천천히 고민해서 풀어보세요. 지금까지 학습한 내용을 모두 동원해야 풀 수 있으며 막힐 때는 지금까지 학습한 내용을 다시 복습하면서 힌트를 찾아보세요.

# 입력
# 3 3
# .**
# *..
# .*.
# 결과
# 2**
# *43
# 2*1
# 입력
# 5 5
# ..*..
# ...*.
# .*...
# .***.
# *.*..
# 결과
# 01*21
# 123*1
# 2*532
# 3***1
# *4*31

matrix = []
row, col = map(int, input().split())

for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        count = 0
        if matrix[i][j] == '.':
            for x in range(-1, 2, 1):
                for y in range(-1, 2, 1):
                    if 0 <= i + x < row and 0 <= j + y < col:
                        if matrix[i+x][j+y] == '*':
                            count += 1
            matrix[i][j] = count

for i in matrix:
    for j in i:
        print(j, sep='', end='')
    print()
