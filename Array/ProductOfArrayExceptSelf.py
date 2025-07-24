import numpy as np

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        new = np.array(nums)
        total = np.prod(new)

        answer = []

        for i in range(l):
            if new[i]!=0:
                answer.append( total / new[i])  
            else:
                newArray = np.prod(np.delete(new,i))
                answer.append(newArray)

        return answer
