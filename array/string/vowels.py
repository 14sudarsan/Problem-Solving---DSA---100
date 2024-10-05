class Solution:
    def count_vowels(self, n):
        count = 0
        for i in range(len(n)):
            if n[i] =="a" or n[i] == "e" or n[i]=="i" or n[i]=="o" or n[i]=="u":  # Checking for vowels in both lowercase and uppercase
                count += 1
        return count

sol = Solution()
print(sol.count_vowels("Hello,World!"))

