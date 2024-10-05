
class Solution:
    def threeSum(self,n, num):
       st = set()
    
       
       
       for i in range(n):
        hashset = set()

        for j in range(i+1,n):
            third =-( num[i]+num[j])
            hashset.add(num[j])
            if third in hashset:
                temp = [num[i],num[j],third]
                temp.sort()
                st.add(tuple(temp))
          
        return [list(triplet) for triplet in st]
        
sol = Solution()

print(sol.threeSum(3,[0,1,1]))

