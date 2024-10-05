class Solution:
    
    def peakIndexInMountainArray(self, arr):
        start = 0
        end = len(arr) - 1
        
        while start < end:
            mid = (start + end) // 2  # Keeping your original mid calculation logic
            
            if mid < end and arr[mid] < arr[mid + 1]:  # Ensure mid + 1 is within bounds
                start = mid + 1
            elif arr[mid] > arr[mid + 1]:
                end = mid
        
        return start  # Return the peak element after the loop

sol = Solution()
print(sol.peakIndexInMountainArray([3,2,1,5,6,4]))

            
        