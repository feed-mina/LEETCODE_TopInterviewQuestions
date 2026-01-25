import math

class Solution:
    def countPrimes(self, n: int) -> int:
        print('n:' , n);
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
                # range(시작, 끝, 간격)의 구조를 숫자로 직접 대입
                # 여기서 간격의 i 만큼의 배수 역할을 한다
                # i * i 의 의미는 예를들어 만약 i가 5라면 5 *2, 5*3, 5*4 는 앞에서 2나 3의 배수로 지워졌다. 그래서 5의 제곱인 25부터 지워도 된다. 

                for j in range(i * i, n , i):
                    is_prime[j] = False

        # 개수 세기 : 마지막에 배열에서 여전히 "소수임"을 남아있는 칸이 몇 개 인지 세기
        
        return is_prime.count(True)

                


        
if __name__ == "__main__":
    obj = Solution()
    answer = obj.countPrimes(10)
    print('answer', answer)
