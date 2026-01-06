# First Bad Version

# Binary Search 이진탐색 : 범위를 절반씩 줄이기 - like 업다운게임

# The isBadVersion API is already defined for you.
# 예를 들어 4번째 버전부터 고장 났다고 가정하는 경우
def isBadVersion(version: int) -> bool:
    first_bad = 4
    if version >= first_bad:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        print("isBadVersion(3)", isBadVersion(3))
        print("isBadVersion(4)", isBadVersion(4))

        low = 1
        high = n
        ans = 0 # 우선 정답을 임의처리


        while low <= high:
            # mid 계산은 반드시 반복문 안으로 넣어야 돌아간다
            mid = (low+high) // 2
            print("현재 탐색 범위:", low, "~", high, "/중앙값 mid:", mid)


            if isBadVersion(mid):
                print("isBadVersion(mid)", isBadVersion(mid))
                # 고장을 찾았다면 우선 이 중간값이 첫번째일수 있으니까 ans로 저장
                ans = mid 
                # 더 앞 번호에 있을수도 있으니 범위를 down
                high = mid - 1
            else:
                # 정답이 중간값보다 클 수 있다. 이럼 up
                low = mid + 1

        return ans


        
if __name__ == "__main__":
    sol = Solution()
    result = sol.firstBadVersion(5)
    print("result", result)
