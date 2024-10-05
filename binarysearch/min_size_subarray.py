class Solution(object):
    def minSubArrayLen(self, target, nums):
        # If the total sum of nums is less than the target, return 0
        if sum(nums) < target:
            return 0

        # If the target is directly in nums, the minimum length is 1
        if target in nums:
            return 1

        # Initialize mini to a large number instead of 2 for correct comparisons
        mini = len(nums) + 1  # max possible length + 1 to ensure it gets updated
        n = len(nums)

        # Iterate through the array
        for i in range(n):
            m = 0
            length = 0

            # Start summing subarray starting from index i
            for j in range(i, n):
                m += nums[j]
                length += 1

                # Once the subarray sum reaches or exceeds the target
                if m >= target:
                    # Update mini with the smallest length found
                    if length < mini:
                        mini = length
                    break  # Exit the inner loop since we've found a valid subarray

        # If mini was never updated, it means no valid subarray was found
        if mini == len(nums) + 1:
            return 0
        
        return mini
sol= Solution()
print(sol.minSubArrayLen(4,[1,4,4]))