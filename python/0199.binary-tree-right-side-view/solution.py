# Created by 林玮 (Jade Lin) at 2026/04/07 18:56
# leetgo: 1.4.15
# https://leetcode.cn/problems/binary-tree-right-side-view/

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(root: Optional[TreeNode], depth: int):
            if root is None:
                return

            if len(ans) <= depth:
                ans.append(root.val)

            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)

        dfs(root, 0)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().rightSideView(root)
    print("\noutput:", serialize(ans, "integer[]"))
