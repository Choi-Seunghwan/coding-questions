"""
  문자열 균형 갯수 세기 문제.
  LR 두 문자가 나타나며, 음수와 양수 영역으로,
  0이 됐을 경우 균형이 맞춰졌다고 보고, result 값을 1 올린다.
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        result = 0

        for ch in s:
            if ch == "L":
                cnt += 1
            else:
                cnt -= 1

            if cnt == 0:
                result += 1
        return result
