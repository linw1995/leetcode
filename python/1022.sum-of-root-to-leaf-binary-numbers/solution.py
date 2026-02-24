# Created by 林玮 (Jade Lin) at 2026/02/24 11:05
# leetgo: 1.4.15
# https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers/

from typing import *
from leetgo_py import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=begin


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return self.iterateTree(root, [])

    def iterateTree(self, root: Optional[TreeNode], stack: List[int]) -> int:
        if root is None:
            return 0

        stack.append(root.val)

        if root.left is None and root.right is None:
            return self.convertNumber(stack)

        ans = self.iterateTree(root.left, stack[:])
        ans += self.iterateTree(root.right, stack)
        return ans

    def convertNumber(self, stack: List[int]) -> int:
        ans = 0
        step = 1

        for i in reversed(stack):
            ans += i * step
            step *= 2

        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().sumRootToLeaf(root)
    print("\noutput:", serialize(ans, "integer"))
