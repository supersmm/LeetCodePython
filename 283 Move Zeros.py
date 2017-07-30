'''# Move Zeroes
The tricky part is that index changes once heading 0 is removed.'''
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    ans = []
    for i in range(n):
        if nums[i] != 0:
            ans.append(nums[i])
    return ans + [0]*(n-len(ans))
    
# You must do this in-place without making a copy of the array.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZero], nums[i] = nums[i], nums[lastNonZero]
                lastNonZero += 1