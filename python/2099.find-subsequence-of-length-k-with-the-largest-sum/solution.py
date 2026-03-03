# Created by 林玮 (Jade Lin) at 2026/03/03 14:38
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-subsequence-of-length-k-with-the-largest-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums, reverse=True)
        wanted_nums = sorted_nums[:k]
        ans = []
        for num in nums:
            if num in wanted_nums:
                wanted_nums.remove(num)
                ans.append(num)
                if len(ans) >= k:
                    break

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSubsequence(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
