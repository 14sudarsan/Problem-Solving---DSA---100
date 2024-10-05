class Solution:
    
    def reversestring(self,s):
        
        s = s.strip()
        
        words = []
        
        char = list(s)
        
        n = len(char)
        
        
        i = 0
        
        while i<n:
            
            
            while i< n and char[i] == " ":
                
                i = i+1
                
                
            start = i
            
            while i < n and char[i]!=" ":
                
                
                i = i+1
                
            if start < i:
                
                word = "".join(char[start:i])
                
                words.append(word)
                
        words.reverse()
            
        reverse = " ".join(words)
            
        return reverse
                
            
            
            
            
            
            
            
            
            
            
            
            
            
          
sol = Solution()

print(sol.reversestring(str(input("enter the string"))))
                
                    
                    
                    
                
                
                
                