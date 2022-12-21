#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r=0,1
        maxp=0
        n=len(prices)
        while(r<n):
            if(prices[l]<prices[r]):
                profit=prices[r]-prices[l]
                maxp=max(profit,maxp)
            else:
                l=r
            r+=1
        return maxp
