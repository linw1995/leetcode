# Created by 林玮 (Jade Lin) at 2026/03/10 16:10
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-median-from-data-stream/

from typing import *
from leetgo_py import *

# @lc code=begin

from heapq import heappush, heappushpop


class MedianFinder:
    def __init__(self):
        # max < min
        self.max = []
        self.min = []

    def addNum(self, num: int) -> None:
        min, max = self.min, self.max

        if (len(max) + len(min)) & 1 == 0:
            if max and -max[0] > num:
                num = -heappushpop(max, -num)

            heappush(min, num)
        else:
            if min and min[0] < num:
                num = heappushpop(min, num)

            heappush(max, -num)

    def findMedian(self) -> float:
        min, max = self.min, self.max
        if (len(min) + len(max)) & 1 == 0:
            return (min[0] - max[0]) / 2
        else:
            return min[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MedianFinder()

    for i in range(1, len(ops)):
        match ops[i]:
            case "addNum":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                obj.addNum(num)
                output.append("null")
            case "findMedian":
                ans = serialize(obj.findMedian())
                output.append(ans)

    print("\noutput:", join_array(output))
