def solution(people, limit):
    people.sort()
    count = 0
    l = 0
    r = len(people) - 1

    while l <= r:
        p = people[r]
        if limit - p >= people[l]:
            l += 1

        r -= 1
        count += 1

    return count