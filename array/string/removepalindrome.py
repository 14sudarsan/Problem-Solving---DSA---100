class Solution:
    
    def is_palindrome(self,string):
        
        if len(string)==1:
            
            return False
        
        if string == string[::-1]:
            
            
            return string
        
        
    def remove_palidrome(self,sentecnce):
        
        
        array = sentecnce.split()
        
        print(array)
        
        remainwords = [word for word in array if not self.is_palindrome(word)]
        
        
        return " ".join(remainwords)
    
    
sol = Solution()
print(sol.remove_palidrome("malayalam is a string"))