# First Unique Character in a String

# 문자열 s가 주어졌을 때, 첫 번째 반복되지 않는 문자를 찾아서 인덱스를 반환합니다. 문자열이 존재하지 않으면 -1을 반환합니다.

class Solution:
        def firstUniqChar(self, s: str) -> int:
                # answer = -1;

                print("s: ", s);
                # s를 리스트로 바꾸려면 list () 사용
                print("list(s): ", list(s));
                listStr = list(s)
                for i in range(len(listStr)):
                        print("listStr[i]:", listStr[i])
                        print("s.count(listStr[i])", s.count(listStr[i]))

                        # rfind 는 reversed find 와 같다 뒤에서부터 검사, 어쩌면 투포인트 느낌
                        if s.find(listStr[i]) == s.rfind(listStr[i]):
                        # if s.count(listStr[i]) == 1:
                                #answer = i Early Stop에 익숙해지자
                                return i 
                # 중복값이 없으면 -1
                return -1
        
if __name__ == "__main__":
    obj = Solution()
    answer = obj.firstUniqChar("loveleetcode")
    print('answer', answer)
