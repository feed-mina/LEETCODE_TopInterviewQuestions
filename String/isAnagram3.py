from collections import defaultdict, Counter

class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
                if len(s) != len(t):
                        return False
                        
                count = defaultdict(int);
                print("Counter(s)", Counter(s));
                print("Counter(t)", Counter(t));
                for char in s:
                        count[char] += 1

                for char in t:
                        if count[char] == 0:
                                print("count[char]: ", count[char]);
                                return False
                        count[char] -= 1
                        print("count[char]: ", count[char]);

                return True
        # 또는 Counter로 한번에 해겨랗ㄹ수 있음 
        # 두 단어의 구성 성분(문자별 개수)이 완벽히 일치하는지 비교
                #return Counter(s) == Counter(t)



        
        
if __name__ == "__main__":
    obj = Solution()
    answer = obj.isAnagram("anagram", "nagaram")
    print('answer', answer)
