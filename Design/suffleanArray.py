from typing import List
import random 

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)
        

    def reset(self) -> List[int]:
        # 원본 self.original를 기본으로 다시 리스트를 만든다 
        # 그걸 self.nums 에 넣는
        self.nums =  list(self.original)
        return self.nums
        

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            j = random.randint(i, len(self.nums) -1)
            # random.randint(a,b) 는 a부터 b까지 중 하나의 숫자를 무작위로 뽑아준다
            self.nums[i], self.nums[j] = self.nums[j],self.nums[i]
            # i번째 방에 있는 값과 j번째 방에 있는 값을 서로 맞바꿔라

            pass
        return self.nums


        
if __name__ == "__main__":
    obj = Solution([1, 2, 3])
    param_1 = obj.reset()
    param_2 = obj.shuffle()
    print("param_1", param_1)
    print("param_2", param_2)
