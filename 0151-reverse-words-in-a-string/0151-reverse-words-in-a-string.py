class Solution:
    def reverseWords(self, s: str) -> str:
        s+=' '
        word=''
        s1=''
        for i in range(len(s)):
            if i!=len(s)-1:
                if s[i] ==' 'and s[i+1]==' ':
                    continue
            if s[i].isalnum():
                word+=s[i]
            else:
                s1=word+' '+s1
                word=''
        if s1[-2]==' ':
            return s1[:-2]
        return s1[:-1]