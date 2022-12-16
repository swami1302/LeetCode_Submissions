class Solution:
    def isHappy(self, n: int) -> bool:
        v=set() #using Set in order for fast memory
        while n not in v:
            v.add(n)
            n=self.sumOfsquares(n)

            if n==1:
                return True
        return False

    def sumOfsquares(self,n: int):
        sum=0
        while n: #traversing the squares of the number
            digit=n%10
            digit=digit**2
            sum+=digit
            n=n//10
        return sum
