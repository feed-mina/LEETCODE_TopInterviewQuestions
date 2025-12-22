class Solution:
    def reverse(self, x: int) -> int:
        print("함수시작")

        sign = 1
        if x < 0:
            sign = -1
            x = -x 
            print("음수 -> 양수로 바꿔서 처리")
        else:
            print("양수")

            res = 0 
            sample = 0
            while x > 0:
                pop = x % 10
                print("현재 x",x)
                print("나머지, 맨뒷자리", x%10)
                x  = x//10
                print("줄어든x값",x)
                res = res * 10 + pop
                # 값에 나머지를 더하고 두번째부터 나머지에 10 곱한 값을 순서대로 더해준다.
                sample = sample * 10 + x%10
                print('res(뒤집는중)',res)
                print('---')
            res *= sign

            if res < -2**31 or res > 2**31 -1:
                return 0
              
            return res


if __name__ == "__main__":
    sol = Solution()
    result = sol.reverse(123)
    print("result", result)
