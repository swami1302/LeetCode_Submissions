//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution {
public:
    int maxProfit(vector<int>& v) {
        int minm=v[0];
        int profit=0;
        for(int i=0;i<v.size();i++){
            minm= min(minm,v[i]);
            int current=v[i]-minm;
            profit=max(profit,current);
        }
        return profit;
    }
};
