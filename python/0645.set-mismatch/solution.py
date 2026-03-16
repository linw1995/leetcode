# Created by 林玮 (Jade Lin) at 2026/03/16 21:47
# leetgo: 1.4.15
# https://leetcode.cn/problems/set-mismatch/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        deprecated_num = 0
        missing_num = 0
        i = 0
        target = 1
        size = len(nums)
        while i < size:
            num = nums[i]

            if target != num:
                missing_num = target
                target = num


            if i < size - 1 and nums[i + 1] == num:
                deprecated_num = num
                i += 1

            target += 1
            i += 1

        if missing_num == 0:
            missing_num = target

        return [deprecated_num, missing_num]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findErrorNums(nums)
    print("\noutput:", serialize(ans, "integer[]"))
