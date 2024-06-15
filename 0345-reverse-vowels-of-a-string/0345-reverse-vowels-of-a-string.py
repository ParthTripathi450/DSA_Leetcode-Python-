class Solution:
    def reverseVowels(self, s: str) -> str:
        s1=list(s)
        l=[]
        l1=[]
        z=1
        for i in range(len(s1)):
            if s1[i] in 'aeiouAEIOU':
                l.append(s[i])
                l1.append(i)
        a=len(l)//2
        if len(l)%2==0:
            for i in range(a,len(l)):
                b=l1[i]
                l1[i]=l1[a-z]
                l1[a-z]=b
                z+=1
            z=1
            for i in range(a,len(l)):
                b=s1[l1[i]]
                s1[l1[i]]=s1[l1[a-z]]
                s1[l1[a-z]]=b
                z+=1
        else:
            for i in range(a):
                b=l[a-i-1]
                l[a-i-1]=l[a+i+1]
                l[a+i+1]=b
            for i in range(a):
                b=s1[l1[a-i-1]]
                s1[l1[a-i-1]]=s1[l1[a+i+1]]
                s1[l1[a+i+1]]=b
        x=''.join(s1)
        return x
        




        