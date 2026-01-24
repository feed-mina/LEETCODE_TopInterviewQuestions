# FizzBuzz.py
 

from typing import List

class Solution:

    def fizzBuzz(self, n: int) -> List[str]:
        print('n:' , n);
        answer = [];
        for i in range(1, n+1):
            if (i % 3 == 0 and i % 5 ==0):
                print('15의 공배수:', i)
                answer.append("FizzBuzz")
            elif i % 3 == 0 :
                print('3의 배수:', i)
                answer.append("Fizz")
            elif i % 5 == 0:
                print('5의 배수: ', i)
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer


# 또는 mactch-case 도 가능하다 
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         answer = []
#         for i in range (1, n+1):
#             match( i % 3 == 0, i % 5 == 0):
#                 case (True, True):
#                     answer.append("FizzBuzz")
#                 case (True, False):
#                     answer.append("Fizz")
#                 case (False, True):
#                     answer.append("Buzz")
#                 case _:
#                     answer.append(str(i))
                
#         return answer
        
        
        
if __name__ == "__main__":
    obj = Solution()
    answer = obj.fizzBuzz(15)
    print('answer', answer)
