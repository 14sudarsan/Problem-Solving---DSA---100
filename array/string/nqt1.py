class Solution:
    def checker(self, entry, exit):
        n = len(entry)
        present = [0] * n
        
        # Iterate through entry and exit to calculate present array
        for i in range(n):
            if i == 0:
                present[i] = entry[i] - exit[i]
            else:
                present[i] = present[i - 1] + entry[i] - exit[i]
        
        return max(present)

sol = Solution()
print(sol.checker([7, 0, 5, 1, 3], [1, 2, 1, 3, 4]))

      
        
            
            
        
        