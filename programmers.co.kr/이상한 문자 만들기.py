def solution(s):
    answer = ""
    arr = s.split(" ")

    for word in arr:
        isOdd = True
        for ch in word:
            if isOdd:
                answer += ch.upper()
            else:
                answer += ch.lower()

            isOdd = not isOdd

        answer += " "

    return answer[:-1]