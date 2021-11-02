from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    values = dict()
    for key, val in enumerate(nums): 
        comp = target - val
        if (comp) in values:
            return [values[comp], key]
        values[val] = key
    return []
#test
nums = [2, 7, 11, 15]
target = 18
ans = twoSum(nums, target)
print(ans)