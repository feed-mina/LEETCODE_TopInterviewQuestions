from typing import List

class Solution:
    def maxProfit(self, prices : List[int]) -> int:   
        if not prices:
            return 0
        # 그리디 알고리즘(Greedy Algorithm)
        # 매 순간순간 가장 최선의 선택(최저가 갱신과 최대 이익 계산)을 하며 나가는 방식 -> 한번의 스캔만으로 정답을 찾을 수 있다. (동전 거스름돈을 줄때 가장 큰 단위의 동전부터 랑 비슷)
        answer = 0
        min_price = prices[0]
        print("min_price", min_price)
        for price in prices:
            print("for문 시작======")
            print("min_price", min_price)
            print("price", price)
            if price < min_price:
                min_price = price
                print("min_price", min_price)
            elif  price - min_price> answer:
                answer = price - min_price
                print("answer", answer)
        print("min_price", min_price)
        print("answer", answer)
        return answer


        
if __name__ == "__main__":
    sol = Solution()
    result = sol.maxProfit([7,5,1,3,6,4])
    print("result", result)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/