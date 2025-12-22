from typing import Optional

# 두 개의 포인터를 서로 다른 속도로 움직이게 해서 거리 차이를 이용하는 투 포인터 기법 
# 포인터 = 지금 보고 있는 위치, 투 포인터 = 위치를 가리키는 변수 2개를 동시에 쓰는 방법 
# 연결 리스트에는 인덱스가 없다. 따라서 연결 리스트용 투 포인터는 속도 차이를 사용한다 , 간격이 핵심 , 속도 차이로 거리 유지. 

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow = dumy
        fast = dummy
        print("초기 상태")
        print("n=",n)
        print("리스트:", end=" ")
        print_list(dummy.next)
        print("slow는 dummy, fast는 dummy")
        print("head.val =", head.val)

# slow 와 fast 간격 차이로 fast가 None 되면 slow 앞에 자리 가 타겟이 된다.         
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
       