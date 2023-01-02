#https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1={}
        d2={}
        l=list(s.split(" "))
        if(len(l)!=len(pattern)):
            return False
        for i in range(len(pattern)):
            if (pattern[i] not in d1) or (l[i] not in d2):
                d1[pattern[i]]=l[i]
                d2[l[i]]=pattern[i]
            elif (pattern[i] in d1 and d1[pattern[i]]!=l[i]):
                return False
        # res = len(list(set(list(d.values()))))
        # if res==1 and res!=len(d):
        #     return False
        if len(d1)!=len(d2):
            return False
        return True
