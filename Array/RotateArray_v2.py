# Rotate Array
# 정수 배열 수가 주어졌을 때, 배열을 오른쪽으로 k만큼 회전시키세요. 여기서 k는 음수가 아닙니다.
# 슬라이싱은 파이썬에서 매우 효율적이지만 엄밀히 말하면 잘라낸 조각들을 잠시 저장할 메모리를 사용하게 된다.

# 메모리를 아예 안 쓰는(Reverse) 방식
# 추가 메모리를 거의 쓰지 않고 빅오(1) 공간복잡도이다. , 기존 배열에서 자리만 바꾸는 in-place 방식
# 투포인터 알고리즘 ( 두 손가락이 양쪽 끝에서 시작해서 가운데로 모인다 )
# 배열의 특정구간(시작점~끝점)을 뒤집는 도구(함수)
# 하나는 맨 얖 (start)에서 다른 한나는 맨뒤(end)에서 , 두 값을 서로 맞바꾸고 (Swap)

from typing import List

class Solution:
        def rotate(self, nums: List[int], k: int) -> None:
                
                # 배열의 길이보다 큰 k를 방지하기 위해 나머지 연산 수행
                n = len(nums)
                k = k % n

                
                # 내부 함수 : 특정 구간 뒤집기 도구
                def reverse(start, end):
                        while start < end: # 두 손가락이 만나기 전까지만 반복
                                # 1. 두 값을 서로 바꾼다
                                nums[start], nums[end] = nums[end], nums[start]

                                # 2. 포인터를 가운데로 이동시킨다
                                start += 1
                                end -= 1

                # 3단계 뒤집기 전략 실행
                # 전체를 뒤집는다 (0 ~ n-1)
                reverse(0, n-1)

                # 앞의 k개를 다시 뒤집어 정렬한다 (0 ~ k-1)
                reverse(0, k-1)

                # 나머지 뒷부분을 다시 뒤집어 정렬한다 (k ~ n -1)
                reverse(k, n-1)

                return nums
 
                
if __name__ == "__main__":
    obj = Solution()
    answer = obj.rotate([1,2,3,4,5,6,7],3)
    print('answer', answer)

 