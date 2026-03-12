# Created by 林玮 (Jade Lin) at 2026/03/12 11:04
# leetgo: 1.4.15
# https://leetcode.cn/problems/left-and-right-sum-differences/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        tmp = 0
        for num in nums:
            ans.append(tmp)
            tmp += num

        size = len(ans)
        tmp = 0
        for idx, num in enumerate(reversed(nums)):
            idx = size - idx - 1
            ans[idx] = abs(ans[idx] - tmp)
            tmp += num

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().leftRightDifference(nums)
    print("\noutput:", serialize(ans, "integer[]"))
