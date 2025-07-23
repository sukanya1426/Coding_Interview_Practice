class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        left = 0
        right = 1
        
        maxProfit = 0
        profit = 0

        
        
        while right < l:
            if prices[left] < prices[right]:
                profit = prices[right]-prices[left]
                
                maxProfit = max(maxProfit,profit)
            
            else:
                left=right
            right+=1
            
                

        return maxProfit
            

       
                    
