# Created by 林玮 (Jade Lin) at 2026/04/03 15:20
# leetgo: 1.4.15
# https://leetcode.cn/problems/subsets/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in nums:
            for i in range(len(ans)):
                prev = ans[i]
                new_set = prev[:]
                new_set.append(num)
                ans.append(new_set)

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().subsets(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
