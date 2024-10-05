class Solution:
    
    def possible(self,arr,capacity,endday):
        
        current_sum = 0
        days = 1  # Start with one day
        
        for i in range(len(arr)):
            if current_sum + arr[i] > capacity:
                days += 1  # Need another day
                current_sum = arr[i]  # Start new day with the current element
                if days > endday:  # If days exceed the allowed endday, it's not possible
                    return False
            else:
                current_sum += arr[i]
        
        return True
        
    def binarySearch(self,arr,endday):
        
        start = max(arr)
        
        end = sum(arr)
        
        while start <= end:
            
            mid = start + (end - start)//2
            
            
            check = self.possible(arr,mid,endday)
            
            
            if check == True:
                
                end = mid -1
                
            else:
                
                start = mid +1
                
        return start
    
arr = [1,2,3,4,5,6,7,8,9,10]
endday = 5
sol = Solution()
print(sol.binarySearch(arr,endday))