# Created by 林玮 (Jade Lin) at 2026/03/20 09:50
# leetgo: 1.4.15
# https://leetcode.cn/problems/path-sum-iii/

from typing import *
from leetgo_py import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=begin

from collections import deque


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def rootSum(root: Optional[TreeNode], targetSum: int):
            if root is None:
                return 0

            ans = 0
            targetSum -= root.val
            if targetSum == 0:
                ans += 1

            ans += rootSum(root.left, targetSum)
            ans += rootSum(root.right, targetSum)
            return ans

        if root is None:
            return 0

        ans = rootSum(root, targetSum)
        ans += self.pathSum(root.left, targetSum)
        ans += self.pathSum(root.right, targetSum)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    targetSum: int = deserialize("int", read_line())
    ans = Solution().pathSum(root, targetSum)
    print("\noutput:", serialize(ans, "integer"))
