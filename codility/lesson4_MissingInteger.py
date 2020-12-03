def solution(A):
    # write your code in Python 3.6
    index = None
    temp = list(set(A))
    temp.sort()
    try:
        index = temp.index(1)
    except :
        return 1

    num = 1
    for i in temp[index:]:
        if i != num:
            return num
        num += 1

    return num