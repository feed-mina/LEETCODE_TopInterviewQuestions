#   Intersection of Two Arrays II
# 두 개의 정수 배열 nums1과 nums2가 주어졌을 때, 그들의 교차점 배열을 반환합니다. 결과의 각 요소는 두 배열 모두에 표시된 횟수만큼 나타나야 하며, 어떤 순서로든 결과를 반환할 수 있습니다.
from typing import List

# Counter (빈도수)
class Solution:
        def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

                # [풀이1] 투포인트 : 우선 정렬부터
                nums1.sort()
                nums2.sort()

                # 각 배열을 가리킬 화살표(포인터)
                i, j = 0, 0
                answer = []

                # 둘,중 하나라도 끝에 도달하면 멈춤
                while i < len(nums1) and j < len(nums2):
                        if nums1[i] < nums2[j]:
                                # nums1의 숫자가 더 작으면 더 큰 숫자를 찾기 위해 i를 전진 
                                i += 1
                        elif nums1[i] > nums2[j]:
                                # num2의 숫자가 더 작으면 j를 전진
                                j += 1
                        else:
                                # 숫자가 같다면 교집합 발견!
                                answer.append(nums1[i])
                                i += 1
                                j += 1
                return answer
                        


        
        
if __name__ == "__main__":
    obj = Solution()
    result = obj.intersect([4,9,5], [9,4,9,8,4])
    print('result', result)
