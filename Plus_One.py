#https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, v: List[int]) -> List[int]:
        l=len(v)
        if(v[l-1]<9):
            v[l-1]+=1
            return v
        sum=0
        for i in range(l):
            sum=sum*10+v[i]
        sum+=1
        digit=[]
        while(sum):
            i=sum%10
            digit.append(i)
            sum=sum//10
        return digit[::-1]
