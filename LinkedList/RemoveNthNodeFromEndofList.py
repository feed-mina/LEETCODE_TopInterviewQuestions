from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        print("시작")
        print("n=",n)
        print("head.val =", head.val)
        # 길이 구하기
        length = 0
        cur = head

        while cur:
            print("index값: " ,length,"현재값: ", cur.val)
            cur = cur.next
            length += 1

        print("리스트 길이 =,", length)
        # 2. 앞에서 지울 위치
        target = length - n
        print("지울 index", target)

        # 3. 첫 노드를 지우는 경우
        if target == 0:
            return head.next

        # 4. 지울 노드 앞까지 이동
        cur = head
        idx = 0


        while idx < target - 1:
            cur = cur.next
            idx += 1
            print("현재 노드 ", cur.val)

        # 4. 삭제
        print("삭제 대상 =", cur.next.val)
        cur.next = cur.next.next

        
        return head

def print_list(head):
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()

if __name__ == "__main__":
    # 연결 리스트 만들기: 1 -> 2 -> 3
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    sol = Solution()
     # sol.removeNthFromEnd(n1,2)
    new_head = sol.removeNthFromEnd(n1,2)
    print_list(new_head)
       