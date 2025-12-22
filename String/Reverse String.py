from typing import List

# 투포인트 연습
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left  = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

if __name__ == "__main__":
    sol = Solution()
    result = sol.reverseString(["h","e","l","l","o"])
    print("result", result)
