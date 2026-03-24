class Solution:
    def longestPrefix(self, s: str) -> str:
        n=len(s)
        lps=[0]*n
        i=1
        curr=0
        while i<n:
            if s[i]==s[curr]:
                curr+=1
                lps[i]=curr
                i+=1
            else:
                if curr!=0:
                    curr=lps[curr-1]
                else:
                    lps[i]=0
                    i+=1
        l=lps[n-1]
        return s[:l]