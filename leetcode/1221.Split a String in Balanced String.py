class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        result = 0
        
        for ch in s:
            if ch == 'L':
                cnt += 1
            else:
                cnt -= 1
            
            if cnt == 0:
                result += 1
        return result