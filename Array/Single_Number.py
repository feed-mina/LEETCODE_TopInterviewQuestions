# 136. Single Number
# 비어 있지 않은 정수 수 배열이 주어졌을 때, 하나를 제외한 모든 원소가 두 번 나타납니다. 그 하나를 구합니다.
# 선형 실행 시간 복잡도를 가진 솔루션을 구현하고 일정한 여분의 공간만 사용해야 합니다.


from typing import List

class Solution:
        def singleNumber(self, nums: List[int]) -> int:
                # 0으로 시작해야 어떤 숫자가 들어와도 그 숫자 그대로 유지된다.
                answer = 0
                n = len(nums)
                for num in nums:
                        # 기존 answer과 새로운 숫자를 XOR연산하고 answer를 업데이트 
                        # answer = answer ^ num 과 같은 의미
                        answer ^= num 
                return answer

        
        
if __name__ == "__main__":
    obj = Solution()
    result = obj.singleNumber([4,1,2,1,2])
    print('result', result)
