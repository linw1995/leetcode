# Created by 林玮 (Jade Lin) at 2026/03/15 20:15
# leetgo: 1.4.15
# https://leetcode.cn/problems/max-consecutive-ones/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMaxConsecutiveOnes(nums)
    print("\noutput:", serialize(ans, "integer"))
