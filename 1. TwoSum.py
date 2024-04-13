# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i_index, i_value in enumerate(nums):
            number = i_value
            for j_index, j_value in enumerate(nums):
                if i_index != j_index:
                    sum_number = i_value + j_value
                    if sum_number == target:
                        return [i_index, j_index]
