class Solution(object):
    def jump(self, nums):
        
        currentposition = 1

        jumps  = 0

        while currentposition < len(nums)-1:

            jumps = jumps+2

            currentposition = currentposition+ nums[currentposition]

            return jumps
sol = Solution()
sol.jump([2,3,1,1,4])