class Solution:
    def targetIndices(self, nums, target):
        nums.sort()
        return [i for i, val in enumerate(nums) if val == target]
