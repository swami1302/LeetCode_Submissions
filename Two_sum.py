#https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            new = target-nums[i]
            if new in d:
                return [d[new],i]
                
            else:
                d[nums[i]]=i
