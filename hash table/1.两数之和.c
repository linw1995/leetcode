/*
 * @lc app=leetcode.cn id=1 lang=c
 *
 * [1] 两数之和
 *
 * https://leetcode-cn.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (46.74%)
 * Likes:    7307
 * Dislikes: 0
 * Total Accepted:    756.8K
 * Total Submissions: 1.6M
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * 给定一个整数数组 nums 和一个目标值
 * target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
 *
 * 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
 *
 * 示例:
 *
 * 给定 nums = [2, 7, 11, 15], target = 9
 *
 * 因为 nums[0] + nums[1] = 2 + 7 = 9
 * 所以返回 [0, 1]
 *
 *
 */

// @lc code=start

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
typedef struct {
  int id;            /* locOfNums */
  int val;           /* key */
  UT_hash_handle hh; /* makes this structure hashable */
} candidateHashEntry;

void addCandidate(candidateHashEntry **candidates, int candidateId,
                  int candidateVal) {
  candidateHashEntry *candidate = malloc(sizeof(candidateHashEntry));
  candidate->id = candidateId;
  candidate->val = candidateVal;
  HASH_ADD_INT(*candidates, val, candidate);
}

candidateHashEntry *findCandidate(candidateHashEntry *candidates,
                                  int candidateVal) {
  candidateHashEntry *candidate = NULL;
  HASH_FIND_INT(candidates, &candidateVal, candidate);
  return candidate;
}

int *twoSum(int *nums, int numsSize, int target, int *returnSize) {
  candidateHashEntry *candidates = NULL;
  for (int i = 0; i < numsSize; i++) {
    candidateHashEntry *candidate = findCandidate(candidates, target - nums[i]);

    if (candidate != NULL) {
      *returnSize = 2;
      int *ans = malloc(sizeof(int) * 2);
      ans[0] = candidate->id;
      ans[1] = i;
      return ans;
    }

    addCandidate(&candidates, i, nums[i]);
  }

  *returnSize = 0;
  return NULL;
}

// @lc code=end
