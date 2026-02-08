# Created by 林玮 (Jade Lin) at 2026/02/08 10:00
# leetgo: 1.4.15
# https://leetcode.cn/problems/balanced-binary-tree/

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, balanced = self.calculateDepth(root)
        return balanced

    def calculateDepth(self, root: Optional[TreeNode]) -> Tuple[int, bool]:
        if root is None:
            return 0, True
        else:
            left_depth, left_balanced = self.calculateDepth(root.left)
            right_depth, right_balanced = self.calculateDepth(root.right)
            return max(
                left_depth, right_depth
            ) + 1, left_balanced and right_balanced and abs(
                left_depth - right_depth
            ) <= 1


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isBalanced(root)
    print("\noutput:", serialize(ans, "boolean"))
