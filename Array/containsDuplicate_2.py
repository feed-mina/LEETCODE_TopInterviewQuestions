from typing import List
from collections import deque

class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
                print("nums: ", nums);
                answer = False
        # set : 중복을 허용하지 않고 순서가 없는 바구니, 순서가 없다 
                seen = set();
                for i in range(len(nums)):
                        num = nums[i] # 리스트의 인덱스 위치 숫자 확인
                         # 이 숫자가 set에 있는지
                        if num in seen:
                                answer = True
                        seen.add(num)

                return answer
        
if __name__ == "__main__":
    obj = Solution()
    answer = obj.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
    print('answer', answer)
