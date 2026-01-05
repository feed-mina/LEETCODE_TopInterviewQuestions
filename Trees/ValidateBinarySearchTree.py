# Validate Binary Search Tree (이진 검색 트리 검증)
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        print("시작")
        if not root:
            return True
        
        # 처음에 스택에 넣을때부터 3개를 넣어야함 (노드, 최소값, 최대값)
        # (현재 노드, 최소 값, 최대 값)
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, low, high = stack.pop()
            print("pop:", node.val, "low:", low, "high:", high)
            # 현재 노드 값이 범위를 지키고 있는지 확인필요
            if not (low < node.val < high):
                return False
        
        # 왼쪽 자식은 현재 부모의 값(node.val) 보다 작아야 하므로 high를 (부모 값)node.val로 설정
        # 오른쪽 자식은 현재 부모의 값(node.val) 보다 커야 하므로 low를 (부모 값)node.val로 설정

            if node.left:
                stack.append((node.left, low, node.val))
                print(" push left:", node.left.val, "new_low:", low, "new_high:", node.val)
            if node.right:
                stack.append((node.right, node.val, high))
                print(" push right:", node.right.val, "new_low:", node.val, "new_high:", high)

        return True


if __name__ == "__main__":
    root = TreeNode(
        2,
        TreeNode(1),
        TreeNode(3)
    )
    sol = Solution()
    result = sol.isValidBST(root)
    print("result", result)
