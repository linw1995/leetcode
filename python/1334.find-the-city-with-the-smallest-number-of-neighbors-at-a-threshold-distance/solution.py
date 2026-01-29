# Created by 林玮 (Jade Lin) at 2026/01/29 09:26
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

from typing import *
from leetgo_py import *

# @lc code=begin

import heapq
import operator


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        d_edges = [[] for _ in range(n)]
        for i, j, w in edges:
            d_edges[i].append((j, w))
            d_edges[j].append((i, w))

        ans = 0
        cnts = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                dst = self.findShortestWeight(n, i, j, d_edges, distanceThreshold)
                # print("found", i, j, dst)
                if dst is not None and dst <= distanceThreshold:
                    cnts[i] += 1
                    cnts[j] += 1

        # print("find all", list(enumerate(cnts)))
        ans = 0
        min_cnt = cnts[0]
        for i, cnt in enumerate(cnts[1:], start=1):
            if min_cnt >= cnt:
                ans = i
                min_cnt = cnt

        return ans

    def findShortestWeight(
        self,
        n: int,
        i: int,
        j: int,
        edges: List[List[Tuple[int, int]]],
        distanceThreshold: int,
    ) -> Optional[int]:
        q = [(w, t) for (t, w) in edges[i]]
        heapq.heapify(q)
        seen = [False] * n
        while q:
            (weight, target) = heapq.heappop(q)

            # print("next", target, weight)
            if target == j:
                return weight
            elif not seen[target]:
                seen[target] = True
                for t, w in edges[target]:
                    if t == i or w > distanceThreshold:
                        continue

                    heapq.heappush(q, (weight + w, t))


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    distanceThreshold: int = deserialize("int", read_line())
    ans = Solution().findTheCity(n, edges, distanceThreshold)
    print("\noutput:", serialize(ans, "integer"))
