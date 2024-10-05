class Solution:
    
    def maxi(self, s):
        max_length = 0
        current_length = 0
        
        for i in range(len(s)):
            if s[i] == "b":
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
            else:
                current_length = 0  # Reset the current length when a different character is found
        
        return max_length

sol = Solution()
print(sol.maxi("bbbaaaababa"))
