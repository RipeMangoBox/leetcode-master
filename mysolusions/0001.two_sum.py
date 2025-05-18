from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i, val in enumerate(nums):
            m[val] = i
        for i, key in enumerate(nums):
            the_other = target - key
            if the_other != key and the_other in m.keys():
                return [i, m[the_other]]
            
            