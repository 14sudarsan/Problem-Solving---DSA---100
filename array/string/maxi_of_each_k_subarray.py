class Solution:
    def max_subarray(self, nums, k):
        if not nums or k <= 0:
            return []

        lst = []
        for i in range(len(nums) - k + 1):
            # Find the maximum in the current window of size k
            max_val = nums[i]
            for j in range(1, k):
                if nums[i + j] > max_val:
                    max_val = nums[i + j]
            lst.append(max_val)
        
        return lst

sol = Solution()
print(sol.max_subarray([4, 1, 3, 2, 6], 3))
