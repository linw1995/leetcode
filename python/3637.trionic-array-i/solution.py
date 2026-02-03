# Created by 林玮 (Jade Lin) at 2026/02/03 21:46
# leetgo: 1.4.15
# https://leetcode.cn/problems/trionic-array-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) <= 3:
            return False

        stage = 0
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return False

            if stage in (0, 2) and nums[i - 1] > nums[i]:
                if i == 1:
                    return False

                stage += 1
            elif stage == 1 and nums[i - 1] < nums[i]:
                stage += 1
            elif stage > 2:
                break

        return stage == 2


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().isTrionic(nums)
    print("\noutput:", serialize(ans, "boolean"))
