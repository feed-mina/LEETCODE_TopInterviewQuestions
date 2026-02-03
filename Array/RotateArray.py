# Rotate Array

# 정수 배열 수가 주어졌을 때, 배열을 오른쪽으로 k만큼 회전시키세요. 여기서 k는 음수가 아닙니다.


from typing import List

class Solution:
        def rotate(self, nums: List[int], k: int) -> None:
                # 배열의 길이보다 큰 k를 방지하기 위해 나머지 연산 수행
                k = k % len(nums)

                # k가 0이면 아무것도 할 필요 없음
                if k == 0:
                        return

                # 슬라이싱으로 잘라서 이어 붙이기 
                # nums[:]를 사용하여 원본 배열의 내용을 직접 변경해야함
                nums[:] = nums[-k:] + nums[:-k]
                return nums

        
if __name__ == "__main__":
    obj = Solution()
    answer = obj.rotate([1,2,3,4,5,6,7],3)
    print('answer', answer)

 