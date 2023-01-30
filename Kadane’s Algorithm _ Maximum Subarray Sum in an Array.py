class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            curr_sum = max(curr_sum, 0)
        return max_sum

#To print the subarray, we can keep track of the start and end indices of the subarray and update them if a larger sum is found:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        start, end, s = 0, 0, 0
        for i, num in enumerate(nums):
            if curr_sum < 0:
                curr_sum = num
                s = i
            else:
                curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum
                start = s
                end = i
        return max_sum, nums[start:end+1]
