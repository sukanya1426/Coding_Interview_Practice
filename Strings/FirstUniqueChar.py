from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #to get the count of one alphabate we have to use count[],to get all the count,we have to use Counter()
        count =  Counter(s)
        
        for i in range(len(s)):
            
            if count[s[i]]==1: 
                return i

        return -1
       
        