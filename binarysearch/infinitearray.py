class Infinite:
    
    def __init__(self,arr):
        
        self.arr = arr 
        
        
    def findposition(self, target):
        low  = 0
        
        high = 1
        while  self.arr[high]<target:    
        
           
        
            temp  = high + 1
        #new high is previous end + size of that arr *2
        
            high = high + (high - low +1 )
        
            low = temp
            
        return self.binarysearch(low , high , target)
            
    def binarysearch(self, low , high , target):
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.arr[mid] == target:
                return mid
                # Continue searching in the left half
            if self.arr[mid+1] == target:
                return mid+1    
            elif self.arr[mid] < target:
                low = mid + 1
                
            else:
                high = mid - 1
                
        return -1
arr = [1,3,5,7,8,9,10,13,15,18,20,21,22,23,24,25,26,27,28,29]
searcher = Infinite(arr)

target = 29

position = searcher.findposition(target)

print("element found" , position)

