#include "stdbool.h"
#include "uthash.h"
#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int id;
  int count;
  UT_hash_handle hh;
} hashEntry;

int setCount(hashEntry *set, int num) {
  hashEntry *s = NULL;
  HASH_FIND_INT(set, &num, s);
  if (s == NULL)
    return 0;
  return s->count;
}

int setInc(hashEntry **set, int num) {
  hashEntry *s = NULL;
  HASH_FIND_INT(*set, &num, s);
  if (s == NULL) {
    s = malloc(sizeof(hashEntry));
    s->id = num;
    s->count = 0;
    HASH_ADD_INT(*set, id, s);
  }
  return ++ s->count;
}

int singleNumber(int *nums, int numsSize) {
  hashEntry *set = NULL;
  for (int i = 0; i < numsSize; ++i) {
    setInc(&set, nums[i]);
  }

  for (int i = 0; i < numsSize; ++i) {
    if (setCount(set, nums[i]) == 1) {
      return nums[i];
    }
  }

  return nums[0];
}

int main() {
  int nums[] = {1, 1, 3, 3, 4, 5, 5};
  printf("%d\n", singleNumber(nums, 7));
}

