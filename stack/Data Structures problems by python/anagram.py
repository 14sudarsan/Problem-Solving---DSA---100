class Solution:
    
    def anagram(self,s,t):
        
        count_r = {}
        
        
        for char in s:
            
            if char in count_r:
                
                count_r[char] = count_r[char]+1
            else:
                
                count_r[char] = 1
                
        for char in t:
            
    
                
            if char not in count_r or count_r[char] == 0:
                
                return False
            
            else:
                
                count_r[char] = count_r[char] -1
            
            
        for value in count_r.values():
            
            if value!= 0:
                
                return False
            
        return True
sol = Solution()
print(sol.anagram("anagram","nagaram"))
                
                