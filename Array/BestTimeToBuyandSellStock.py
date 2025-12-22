from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        output = 0

        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
              output += prices[i] - prices[i-1]
        return output

if __name__ == "__main__":
    s = Solution()
    result = s.maxProfit([7,6,4,3,1])
    print("result", result)