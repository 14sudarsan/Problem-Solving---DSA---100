class Solution:
  
    def first_and_last_check(self, arr, t):
        low = 0
        high = len(arr) - 1
        first_occurrence = -1  # Initialize to -1 in case the target is not found
        last_occurrence = -1   # Initialize to -1 in case the target is not found
        
        # Find the first occurrence
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == t:
                first_occurrence = mid
                high = mid - 1  # Continue searching in the left half
                
            elif arr[mid] < t:
                low = mid + 1
                
            else:
                high = mid - 1
        
        # Reset low and high for the last occurrence search
        low = 0
        high = len(arr) - 1
        
        # Find the last occurrence
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == t:
                last_occurrence = mid
                low = mid + 1  # Continue searching in the right half
                
            elif arr[mid] < t:
                low = mid + 1
                
            else:
                high = mid - 1
                
        return [first_occurrence, last_occurrence]
    
sol = Solution()

print(sol.first_and_last_check([1, 2, 2, 2, 3, 4, 5], 1))  # Output: [1, 3]
