# CountPrimes version2

import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        # 저장 공간 만들기 : n개의 방을 가지고 배열을 만들고 모두 "소수임"상태로 시작한다
        #배열 만들기 
        is_prime = [True] * n 
        # 기본값 설정 : 0과 1은 소수가 아니니 "소수아님"으로 표시
        is_prime[0] = False
        is_prime[1] = False

        limit = int(math.sqrt(n))
        # sqrt는 제곱근 함수이다 
        # limit = n ** 0.5
        # 로 바꿔 쓸 수 있다. 제곱을 하는데 0.5는 루트값으로 제곱하는거라서 거듭제곱
        # 또는 while i * i < n : 도 가능하다 
        for i in range(2, limit+1):

        # 거르기 작업 : 2부터시작해서 루트 n까지 숫자를 하나씩 확인

            if is_prime[i]:
                # 슬라이싱을 이용해 i의 배수들을 한번에 False
                # False로 바꿀 개수만큼 리스트를 만들어 대입한다
                count = len(range(i * i, n , i))
                print('count: ', count)
                is_prime[i * i : n : i ] = [False] * count

        # 개수 세기 : 마지막에 배열에서 여전히 "소수임"을 남아있는 칸이 몇 개 인지 세기
        
        return is_prime.count(True)


        
if __name__ == "__main__":
    obj = Solution()
    answer = obj.countPrimes(20)
    print('answer', answer)
