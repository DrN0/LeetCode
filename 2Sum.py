class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            ix_rest_list = range(i+1,len(nums))
            for j in ix_rest_list:
                if nums[i] + nums[j] == target:
                    return [i, j]
                    
# Details 
# Runtime: 48 ms, faster than 72.70% of Python3 online submissions for Two Sum.
# Memory Usage: 14.2 MB, less than 95.87% of Python3 online submissions for Two Sum.
