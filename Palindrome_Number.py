

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return 0
        else:
            rev=0
            temp=x
            rem=0
            while(temp):
                rem=temp%10
                rev=rev*10+rem
                temp=temp//10
            if(rev==x):
                return 1
            return 0
