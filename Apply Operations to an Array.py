class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        pos = 0 
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        for i in range(pos, n):
            nums[i] = 0
        
        return nums
