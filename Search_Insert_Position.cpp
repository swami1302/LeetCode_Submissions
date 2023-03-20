//https://leetcode.com/problems/search-insert-position/description/

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int c=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==target) return i;
        }
        for(int i=0;i<nums.size();i++){
            if(target<nums[i]){
            return i;
            //c=1;
            //break;
            }
        }
        if(c==0){
        return nums.size();
        }
        return 0;
        
    }
};
