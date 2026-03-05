# Plus One
# 정수 배열 숫자로 표시되는 큰 정수가 주어지는데, 여기서 각 숫자[i]는 정수의 i번째 숫자입니다. 숫자는 왼쪽에서 오른쪽 순서대로 가장 큰 숫자부터 가장 작은 숫자까지 순서가 매겨집니다. 큰 정수에는 앞의 0이 포함되어 있지 않습니다.
# 큰 정수를 하나씩 증가시키고 결과적인 자릿수 배열을 반환합니다.

from typing import List


class Solution:
        def plusOne(self, digits: List[int]) -> List[int]:
                answer = []
                # 1. 리스트의 숫자들을 문자열로 바꿔서 하나로 합침
                # map(str, digits) -> ['9']
                # "".join(...) -> "9"
                combined_str = "".join(map(str, digits))
                num = int(combined_str)
                print('num',num)
                num_2 = num + 1

                # 다시 문자열로 바꿔서 하나씩 리스트에 담기
                for i in str(num_2):
                        # i는 "1", "0" 같은 문자열이므로 다시 숫자로 바꿔서 추가
                        answer.append(i)
                # for 문이 다 끝난뒤에 결과 반환
                # answer = [int(i) for i in str(num)] 은 위와 같음 (리스트 컴프리헨션)

                return answer

        
        
if __name__ == "__main__":
    obj = Solution()
    result = obj.plusOne([9])
    print('result', result)
