class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum_count = {0: 1}  
        prefix_sum = 0
        count = 0
     # sliding Window 
        for i in nums:
            prefix_sum += i
            diff = prefix_sum - goal
            if diff in prefix_sum_count:
                count += prefix_sum_count[diff]
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

        return count