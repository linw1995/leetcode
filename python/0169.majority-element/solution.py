# Created by 林玮 (Jade Lin) at 2026/03/10 16:34
# leetgo: 1.4.15
# https://leetcode.cn/problems/majority-element/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        cnt = 1
        for vote in nums[1:]:
            if vote != ans:
                cnt -= 1
            else:
                cnt += 1

            if cnt == 0:
                ans = vote
                cnt = 1

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().majorityElement(nums)
    print("\noutput:", serialize(ans, "integer"))
