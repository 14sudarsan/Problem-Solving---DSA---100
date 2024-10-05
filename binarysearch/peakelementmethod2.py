class Solution:
    
    def peakelement(self, arr):
        n = len(arr)
        
        # Edge case: single element
        if n == 1:
            return arr[0]
        
        # Check first and last elements
        if arr[0] > arr[1]:
            return arr[0]
        
        if arr[n - 1] > arr[n - 2]:
            return arr[n - 1]
        
        start = 1
        end = n - 2
        
        while start <= end:
            mid = start + (end - start) // 2
            
            # Check if mid is the peak element
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return arr[mid]
            
            # If mid is greater than the next element, the peak is in the left half
            if arr[mid] < arr[mid + 1]:
                start = mid+1
            else:
                end = mid-1
        
        return -1
    
sol = Solution()
print(sol.peakelement([1,2,3,5,2,0]))