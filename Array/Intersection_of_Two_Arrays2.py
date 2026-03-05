#   Intersection of Two Arrays II
# 두 개의 정수 배열 nums1과 nums2가 주어졌을 때, 그들의 교차점 배열을 반환합니다. 결과의 각 요소는 두 배열 모두에 표시된 횟수만큼 나타나야 하며, 어떤 순서로든 결과를 반환할 수 있습니다.

from typing import List
from collections import Counter

# Counter (빈도수)
class Solution:
        def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
                c1 = Counter(nums1)
                c2 = Counter(nums2)

                # 교집합 연산 (&)을 하면 공통된 숫자의 최소 개수만 남는다.
                intersection = c1 & c2

                # Counter 객체를 리스트로 변환
                # elements()는 각 요소를 개수만큼 반복해서 꺼내줌
                return list(intersection.elements())

        
        
if __name__ == "__main__":
    obj = Solution()
    result = obj.intersect([4,9,5], [9,4,9,8,4])
    print('result', result)

