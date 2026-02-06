class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
                if len(s) != len(t):
                        return False
                scount = {}
                tcount = {}
                
                for char in s:
                        scount[char] =scount.get(char, 0) + 1
                        print("scount ", scount);

                for char in t:
                        tcount[char] = tcount.get(char, 0) + 1
                        print("tcount", tcount)
# 파이썬은 두 딕셔너리에 담긴 키(문자) 와 값(개수)가 모두 일치하면 True, 하나라도 다르면 False를 반환한다.
                return scount == tcount
                        
        
        
if __name__ == "__main__":
    obj = Solution()
    answer = obj.isAnagram("anagram", "nagaram")
    print('answer', answer)
