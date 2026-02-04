# containsDuplicate
# 정수 배열 번호가 주어졌을 때, 배열에 어떤 값이 두 번 이상 나타나면 true로 반환하고, 모든 요소가 구별되면 false로 반환합니다.


from typing import List
from collections import deque

class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
                print("nums: ", nums);
                answer = False
        # set : 중복을 허용하지 않고 순서가 없는 바구니, 순서가 없다 
                seen = set(nums);
                print("seen: ", seen);
                # 중복이 되면 리스트와 세트의 길이가 다름
                if len(nums) == len(seen):
                     answer =  True
                else: answer = False

                return answer
                # return len(nums) != len(set(nums)) 
                # 이걸로 한번에 가능
        
if __name__ == "__main__":
    obj = Solution()
    answer = obj.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
    print('answer', answer)

