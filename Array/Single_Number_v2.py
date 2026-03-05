# 136. Single Number
# 비어 있지 않은 정수 수 배열이 주어졌을 때, 하나를 제외한 모든 원소가 두 번 나타납니다. 그 하나를 구합니다.
# 선형 실행 시간 복잡도를 가진 솔루션을 구현하고 일정한 여분의 공간만 사용해야 합니다.

from typing import List
from collections import Counter

# Counter (빈도수)
# set(중복을 허용하지 않음) 
class Solution:
        def singleNumber(self, nums: List[int]) -> int:
                # [풀이2] 2 * (중복 없는 원소들의 합) - (전체 원소들의 합) = 한번만 나나타는 숫자
                # [풀이2]
               return 2 * sum(set(nums)) - sum(nums)

                # [풀이3]
                # 각 숫자의 빈도수를 계산 
                # counts = Counter(nums)
                # # 빈도수가  1인숫자반환 
                # for num in counts: 
                #         if counts[num] == 1:
                #                 return num


        
        
if __name__ == "__main__":
    obj = Solution()
    result = obj.singleNumber([4,1,2,1,2])
    print('result', result)
