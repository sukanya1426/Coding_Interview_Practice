class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = 0
        maxSum = float('-inf')   #why do we need -inf here ? if we dont then 0 will be greater thn the sum of neg number always

        if len(nums)==1:
            return nums[0]

        for i in range(len(nums)):   #[-2,-1]
            currSum = max(nums[i],currSum+nums[i]) # (-2,-2) -> -2 (-1,-3)-> -1
            maxSum =  max(maxSum,currSum) #(-inf,-2)-> -2   (-2,-1) -> -1

        return maxSum  #-1