class Solution:
    def reverseString(self, s: List[str]) -> None:
        a=len(s)//2
        if len(s)%2!=0:
            for i in range(1,a+1):
                b=s[a+i]
                s[a+i]=s[a-i]
                s[a-i]=b
        else:
            c=(len(s)//2)
            for i in range(0,c):
                b=s[a-1]
                s[a-1]=s[c+i]
                s[c+i]=b
                a-=1
        """
        Do not return anything, modify s in-place instead.
        """
        