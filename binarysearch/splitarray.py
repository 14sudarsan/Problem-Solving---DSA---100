class Solution(object):
    def splitArray(self, nums, target):
        currentsum = 0
        acc = 1
        
        for i in range(len(nums)):
            if currentsum + nums[i] <= target:
                currentsum += nums[i]
            else:
                acc += 1
                currentsum = nums[i]
        
        return acc

    def binarysearch(self, nums, k):
        start = max(nums)
        end = sum(nums)
        
        while start <= end:
            mid = start + (end - start) // 2
            acc = self.splitArray(nums, mid)
            
            if acc <= k:
                end = mid - 1
            else:
                start = mid + 1
        
        return start

sol = Solution()

nums = [7, 2, 5, 10, 8]
k = 2

result = sol.binarysearch(nums, k)
print(result)
