class Solution:
    
    def constructstring(self,s1,s2,r):
        
        if len(s1)+len(s2) != len(r):
            
            return False
        
        
        count = {}
        
        for char in r:
            
            if char in count:
                
                count[char] = count[char]+1
                
            else:
                count[char] = 1
                
        
        combined = s1+s2
        
        for char in combined:
            
            if char not in count or count[char]== 0:
                
                return "No"
            
            else:
                
                count[char] = count[char]-1
                
        for value in count.values():
            
            if value!= 0:
                
                return False
            
        return True
s1 = input("enter the firstname").strip()
s2 = input("enter the secondname").strip()
r = input("enter the name to be checked").strip()

sol = Solution()

print(sol.constructstring(s1,s2,r))
                