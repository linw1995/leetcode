/*
 * @lc app=leetcode.cn id=209 lang=c
 *
 * [209] 长度最小的子数组
 *
 * https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
 *
 * algorithms
 * Medium (39.90%)
 * Likes:    217
 * Dislikes: 0
 * Total Accepted:    33.3K
 * Total Submissions: 79.5K
 * Testcase Example:  '7\n[2,3,1,2,4,3]'
 *
 * 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s
 * 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
 *
 * 示例: 
 *
 * 输入: s = 7, nums = [2,3,1,2,4,3]
 * 输出: 2
 * 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
 *
 *
 * 进阶:
 *
 * 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
 *
 */

// @lc code=start
#define __WITH_LOG__

#ifdef __WITH_LOG__
#include <stdio.h>
#define LOG(message, args...)                                                  \
  fprintf(stdout, "| %s:%d | " message "\n", __FUNCTION__, __LINE__, ##args)
#else
#define LOG(message, args...)
#endif
int minSubArrayLen(int s, int *nums, int numsSize) {
  if (numsSize <= 0)
    return 0;

  int begin = 0, end = 1, sum = nums[0], minLen = numsSize + 1;
  while (begin < end && begin < numsSize) {
    LOG("sum(nums[%d:%d])=%d len=%d minlen=%d", begin, end, sum, end - begin,
        minLen);
    if (sum >= s) {
      if (end - begin < minLen)
        minLen = end - begin;
      sum -= nums[begin++];
    } else if (end < numsSize) {
      sum += nums[end++];
    } else {
      break;
    }
  }
  return minLen == numsSize + 1 ? 0 : minLen;
}

// @lc code=end
