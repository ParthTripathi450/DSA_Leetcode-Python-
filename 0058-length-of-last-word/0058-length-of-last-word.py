class Solution(object):
    def lengthOfLastWord(self, s):
        stripped=s.strip()
        l=stripped.split(" ")
        l1=len(l[-1])
        return l1
        
        