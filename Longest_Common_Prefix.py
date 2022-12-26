#https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        n=len(strs)
        if n==0:
            return ""
        strs.sort()
        first=strs[0]
        last=strs[n-1]
        for i in range(len(first)):
            if first[i]!=last[i]:
                break
            else:
                res+=first[i]
        return res
