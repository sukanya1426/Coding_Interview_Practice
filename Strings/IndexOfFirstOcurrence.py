class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
     
        for i in range(len(haystack)):  # haystack = hello     needle = ll
            if haystack[i:len(needle)+i]==needle:  #this part will check [0,2]->he [1,3]->el [2,4]->ll = ll
                return i      # will return 2
            
        