class Solution(object):
    def strStr(self, haystack, needle):
        

        if not needle:
            return 0
        
        
        for i in range((len(haystack) - len(needle))+1):
            
            
            for j in range(len(needle)):
                
                if haystack[i+j]!=needle[j]:
                    
                    break
                
                if j == len(needle)-1:
                    
                    return i 
        return -1
sol = Solution()

print(sol.strStr("sadbutsad","sad"))
                    
                    