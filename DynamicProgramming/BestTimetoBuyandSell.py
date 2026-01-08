from typing import List

class Solution:
    def maxProfit(self, prices : List[int]) -> int:   
        answer = 0
        for i in range(0, len(prices)):
            # 기준점 : prices[i]
            price = prices[i]
            print("price", price)

            for j in range( i + 1, len(prices)):
                # 비교대상 : prices[j]
                # print("이익이 가장 클때", prices[j] - prices[i])
                maxProfitprice = prices[j] - prices[i]
                if maxProfitprice > answer:
                    answer = maxProfitprice
                # 최소값이 최대값보다 이전에 있는 경우가 없을때 return 0 => maxProfitprice 값 중 양수 값이 하나라도 있다면 0이 안된다. maxProfitprice 중에서 가장 큰 값을 return maxProfitprice 한다.

        return answer
        # Time Complexity: O(n^2) Submission Result: Time Limit Exceeded 이 문제가 발생한다.


        
if __name__ == "__main__":
    sol = Solution()
    result = sol.maxProfit([7,1,5,3,6,4])
    print("result", result)
