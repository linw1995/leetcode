#include "stdbool.h"
#include "uthash.h"
#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int id;
  UT_hash_handle hh;
} hashEntry;

bool setHas(hashEntry *set, int num) {
  hashEntry *s = NULL;
  HASH_FIND_INT(set, &num, s);
  return s ? true : false;
}

void setAdd(hashEntry **set, int num) {
  hashEntry *s = malloc(sizeof(hashEntry));
  s->id = num;
  HASH_ADD_INT(*set, id, s);
}

int singleNumber(int *nums, int numsSize) {
  hashEntry *set = NULL;
  int setSum = 0;
  int total = 0;
  for (int i = 0; i < numsSize; ++i) {
    if (setHas(set, nums[i])) {
      setSum += nums[i];
    } else {
      setAdd(&set, nums[i]);
    }
    total += nums[i];
  }

  return total - 2 * setSum;
}

int main() {
  int nums[] = {1, 1, 3, 3, 4, 5, 5};
  printf("%d\n", singleNumber(nums, 7));
}
