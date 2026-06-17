# Created by 林玮 (Jade Lin) at 2026/06/17 23:13
# leetgo: 1.4.15
# https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof/

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
    def flipTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return

        root.left, root.right = self.flipTree(root.right), self.flipTree(root.left)

        return root




# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().flipTree(root)
    print("\noutput:", serialize(ans, "TreeNode"))
