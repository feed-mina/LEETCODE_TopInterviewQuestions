class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
                if len(s) != len(t):
                        return False
                count = {}

                for char in s:
                        if char in count:
                                count[char] += 1
                        else:
                                count[char] = 1

                for char in t:
                        # t의 글자가 count 목록에 있는지 확인
                        if char in count and count[char] >0:
                                # 있다면 재고를 하나 줄임
                                count[char] -= 1
                        else:
                                # 없다면 애너그램이 아님! 
                                return False 

                # 모든 과정이 끝나고 False에 걸리지 안는다면 True
                return True 
if __name__ == "__main__":
    obj = Solution()
    answer = obj.isAnagram("anagram", "nagaram")
    print('answer', answer)
