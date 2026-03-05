# Plus One
# 정수 배열 숫자로 표시되는 큰 정수가 주어지는데, 여기서 각 숫자[i]는 정수의 i번째 숫자입니다. 숫자는 왼쪽에서 오른쪽 순서대로 가장 큰 숫자부터 가장 작은 숫자까지 순서가 매겨집니다. 큰 정수에는 앞의 0이 포함되어 있지 않습니다.
# 큰 정수를 하나씩 증가시키고 결과적인 자릿수 배열을 반환합니다.

from typing import List

# carry (올림)방식
class Solution:
        def plusOne(self, digits: List[int]) -> List[int]:
                n = len(digits)

                # 1. 뒤에서부터 거꾸로 순회
                for i in range(n-1, -1, -1):
                        # 9 보다 작으면 1만 더하고 완료
                        if digits[i] < 9:
                                digits[i] += 1
                                return digits

                        # 9 라면 0으로 만들고 앞자리로 넘어감
                        digits[i] = 0

                        # 루프를 다 돌고 여기까지 오면 모든 자리가 9였다는 뜻이다 
                        # 맨 앞에 1을 넣는다.  ([9, 9] -> [0, 0] -> [1, 0, 0])
                return [1] + digits 

        
        
if __name__ == "__main__":
    obj = Solution()
    print('result 123:', obj.plusOne([1, 2, 3])) # [1, 2, 4]
    print('result 99:', obj.plusOne([9, 9]))     # [1, 0, 0]
