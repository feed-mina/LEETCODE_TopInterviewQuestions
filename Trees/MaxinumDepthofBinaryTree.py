from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
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

            if node.right:
                print(" push right:", node.right.val, "new_d:", d + 1)
                stack.append((node.right, d + 1))

        print("answer:", max_depth + 1)


        return root.val
        
if __name__ == "__main__":
    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7))
    )
    sol = Solution()
    result = sol.maxDepth(root)
    print("result", result)
