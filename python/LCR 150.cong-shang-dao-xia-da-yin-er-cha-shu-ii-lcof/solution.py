# Created by 林玮 (Jade Lin) at 2026/02/09 20:57
# leetgo: 1.4.15
# https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/

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
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        self.append(root, 0, ans)
        return ans

    def append(self, root: Optional[TreeNode], depth: int, ans: List[List[int]]):
        if root is None:
            return

        if depth >= len(ans):
            ans.append([root.val])
        else:
            ans[depth].append(root.val)

        self.append(root.left, depth + 1, ans)
        self.append(root.right, depth + 1, ans)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().decorateRecord(root)
    print("\noutput:", serialize(ans, "integer[][]"))
