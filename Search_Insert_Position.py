#https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        c=0
        if(target in nums):
            return nums.index(target)
        for i in range(n):
            if target<nums[i]:
                return i
                c=1
                break
        if (c==0):
            return n
