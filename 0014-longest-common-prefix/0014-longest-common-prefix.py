class Solution(object):
    def longestCommonPrefix(self, strs):
     a=strs[0]
     if strs=='':
         return ''
     for i in strs[1:]:
         while not i.startswith(a):
             a=a[:-1]
         if i=='':
            return ''
     return a