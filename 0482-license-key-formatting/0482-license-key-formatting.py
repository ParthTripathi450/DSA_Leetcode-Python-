class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace('-','').upper()
        dup,s1=k,''
        for i in range(len(s)-1,-1,-1):
            if k!=0:
                s1=s[i]+s1
                k-=1
            else:
                s1='-'+s1
                s1=s[i]+s1
                k=dup
                k-=1
        return s1
        '''l=[]
        l1=[]
        l2=list(s)
        for i in range(len(s)):
            if s[i]=='-':
                a=i
                break
        for i in range(0,a+1):
            l.append(s[i])
            l2.pop(i)
        for i in range(a+1,len(s)):
            if s[i]!='-':
                l1.append(s[i])
        while l1:
            for i in range(k):
                if l1==[]:
                    break
                l.append(l1[0].upper())
                l1.pop(0)
            l+='-'
        if l[-1]=='-':
            l=l[0:len(l)-1]
        return ''.join(l)'''
        