class Solution:
    def adddigits(self, num):
        if num % 9 == 0 and num != 0:
            return 9
        else:
            while num > 9:
                num = sum(map(int, str(num)))
            return num
        
sol = Solution()
print(sol.adddigits(38))