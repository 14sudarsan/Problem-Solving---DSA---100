class Solution:
   
    def threesum(self,a):
        array = []
        for i in range(0,len(a)):

            myset = set()

            for j in range(1,len(a)):

                third = -(a[i]+a[j])

                myset.add(a[j])
        if(third!=a[i] and third!=a[j] and third not in myset):

                temp = [a[i],a[j],third]

                sorting = sorted(temp)

        array.append(sorting)
        
        print(array)



array = [-1,0,1,2,-1,-4]

sol = Solution()

print(sol.threesum(array))

