class Solution:
    def coinChange(self,coins,amount):
        
        sum = 0
        
        i = 0
        
        j = len(coins)-1
        
        c = 0
        
        if len(coins) == 1:
            
            for char in coins:
                
                if char%2 == 0 and amount%2 !=0:
                    
                    
                    return -1
        
                
                
        
        while i<=j:
            
            while sum <= amount:
                
                sum = sum+coins[j]
                
                c = c+1
                
                if sum > amount:
                    
                    sum = sum - coins[j]
                    
                    c= c-1
                    
                    j = j-1
                    
                
                    
                if sum == amount:
                    
                    
                    return c
                
                
        return -1
sol = Solution()
print(sol.coinChange([2],3))