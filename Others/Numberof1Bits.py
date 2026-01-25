import math

class Solution:
        def hammingWeight(self, n: int) -> int:
                print("n: ", n);
                
                count = 0
                while n > 0:
                        print('n', n)
                        # 현재 n을 2로 나눈 나머지 1인지 확인 , 나머지는 비트값이 된다 
                        if n % 2 == 1:
                                count += 1
# n을 2를 나눈 몫으로 숫자를 줄여나간다. 
# 나머지가 1일때 count 를 +1 하면 이진법에 1 부분만 셀수있다.
#  n // 2는 현재 자릿수를 검사했으니 다음 자릿수 2 ** n 로 넘어간다는 뜻 , 2로 나눌때 마다 이진수의 자릿수를 한칸씩 왼쪽으로 이동하며 검사한다.
# n % 2는 현재 가장 오른쪽에 있는 비트가 0인지 1인지 확인하는 도구
# n // 2는 확인이 끝난 비트를 버리고 다음 비트를 확인하기 위해 숫자를 옆으로 미는 도구
                        n = n // 2


                        print('new n:', n)

                print('count', count)

                return count
               


        
if __name__ == "__main__":
    obj = Solution()
    answer = obj.hammingWeight(8)
    print('answer', answer)
