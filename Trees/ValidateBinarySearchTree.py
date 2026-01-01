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
        stack = [(root, 0)]
        max_depth = 0

        while stack:
            node, d = stack.pop()
            print("pop:", node.val, "d:", d)

            if d > max_depth:
                max_depth = d
                print("update max_depth:", max_depth)

            if node.left:
                print(" push left:", node.left.val, "new_d:", d + 1)
                stack.append((node.left, d + 1))
                print("node.val: ", node.val)
                if node.left.val > node.val:
                    return False

            if node.right:
                print(" push right:", node.right.val, "new_d:", d + 1)
                stack.append((node.right, d + 1))
                print("node.val: ", node.val)
                if node.right.val < node.val:
                    return False
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
