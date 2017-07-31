# Two pointers
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        lastDistinctIndex = 0
        for i in range(len(nums)):
            if nums[i] != nums[lastDistinctIndex]:
                lastDistinctIndex += 1
                nums[i], nums[lastDistinctIndex] = nums[lastDistinctIndex], nums[i]
        return lastDistinctIndex+1