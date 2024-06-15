class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping_s_t = {}
        mapping_t_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in mapping_s_t:
                if mapping_s_t[char_s] != char_t:
                    return False
            else:
                mapping_s_t[char_s] = char_t

            if char_t in mapping_t_s:
                if mapping_t_s[char_t] != char_s:
                    return False
            else:
                mapping_t_s[char_t] = char_s

        return True

        '''
        s=list(s)
        t=list(t)
        L=[]
        L1=[]
        for i in range(len(s)):
            L1.append(i)
        if len(s)!=len(t):
            return False
        elif len(s)==len(t):
            for i in range(len(s)):
                a=0
                for j in range(i,len(s)):
                    if s[i]==s[j] and i!=j:
                        a+=1
                        if a>0:
                            L.append(j)
                            if j in L1:
                                L1.remove(j)
                            if i in L1:
                                L1.remove(i)
                if a>0:
                    L.append(i)
                if len(L)>0:
                    a=t[L[0]]
                    for k in L:
                        if t[k]!=a:
                            return False
        return True
                for k in L:
                    s[k]=t[k]
                L=[]
            for k in L1:
                s[k]=t[k]
            if s==t:
                return True
            else:
                return False             
'''
