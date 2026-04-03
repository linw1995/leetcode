# Created by 林玮 (Jade Lin) at 2026/04/03 15:20
# leetgo: 1.4.15
# https://leetcode.cn/problems/subsets/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums: List[int]) -> frozenset[frozenset[int]]:
            ans = set()

            for i in range(len(nums)):
                ans = ans.union(dfs(nums[:i] + nums[i + 1 :]))

            ans.add(frozenset(nums[:]))
            return ans

        return list(map(list, dfs(nums)))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().subsets(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
