# Climbing Stairs


 
class Solution:
    def climbStairs(self, n: int) -> int:  
        print("n", n)

        if n == 1 :
            return 1
        #if n == 2:
         #   return 2

      # first = 1
       # second = 2 

        first, second = 1, 2        
       # print("=============")

        for i in range(3, n+1):
           # current = first + second
           # print("current", current)
            # 다음층 계산을 위해 이전의 두번째 값을 첫번째 자리로 이동
            # first = second
            # print("first", first)
            # second = current
            # 다음층 계산을 위해 방금 구한 현재값을 두번째로 옮긴다
           # print("second", second)
           # print("=============")
            first, second = second, first + second
        return second


        
if __name__ == "__main__":
    sol = Solution()
    result = sol.climbStairs(7)
    print("result", result)
