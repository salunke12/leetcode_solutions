class Solution(object):
    def findMaxAverage(self, nums, k):
        cur_sum = sum(nums[:k])
        max_sum = cur_sum

        for i in range(k, len(nums)):
            cur_sum = cur_sum + nums[i] - nums[i-k]

            if cur_sum > max_sum:
                max_sum = cur_sum
        return float(max_sum)/k