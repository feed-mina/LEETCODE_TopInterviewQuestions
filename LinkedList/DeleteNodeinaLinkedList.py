class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, node):
        print("시작")

        print("node.val =", node.val)
        node.val = node.next.val
        node.next = node.next.next

        if node.next:
            print("node.next.val =", node.next.val)
            
        else:
            print("node.next = None")

        print("node 객체 자체 =", node)
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

if __name__ == "__main__":
    # 연결 리스트 만들기: 1 -> 2 -> 3
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)

    n1.next = n2
    n2.next = n3

    sol = Solution()
    sol.deleteNode(n1)
       