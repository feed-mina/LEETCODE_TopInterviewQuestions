import math

# hammingDistance : 두 숫자나 문자열이 서로 얼마나 다른지를 측정하는 방법, 주로 통신 오류를 확인하거나 데이터의 차이를 계산할때 사용
# 같은 길이를 가진 두 데이터 사이에서 서로 다른 무자가 나타나는 위치의 개수를 세는 것
# 두 이진수(0과 1로 이루어진 수)에서 같은 위치에 있는 숫자가 서로 다른 경우의 총 개수 

# XOR (배타적 논리합) 연산 : 두 비트가 다를때 1을 결과로 내놓는 연산, ^ 기호로 사용
# 끝자리가 1인지 확인하는 법 : 숫자 & 1 에서 결과가 1이면 끝자리가 1이고 0이면 끝자리가 0이다.




class Solution:
        def hammingDistance(self, x: int, y: int) -> int:
                # 두 수의 차이를 비트로 나나탠다.
                xor_result = x ^ y
                distance = 0

                # 확인할 비트가남아있는 동안 반복한다
                while xor_result > 0:
                        # 가장 오른쪽 비트가 1인지 확인하고더한다 
                        distance += xor_result & 1

                        # 확인한 비트는 오른쪽으로 밀어서 버린다
                        xor_result = xor_result >> 1

                return distance

        
if __name__ == "__main__":
    obj = Solution()
    answer = obj.hammingDistance(1,4)
    print('answer', answer)
