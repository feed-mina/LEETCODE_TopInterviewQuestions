from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> List[str]:
        r = []
        for i in range(1, len(s)+1):
            r.append(s[len(s) - i])
        return r

if __name__ == "__main__":
    sol = Solution()
    result = sol.reverseString(["h","e","l","l","o"])
    print("result", result)
