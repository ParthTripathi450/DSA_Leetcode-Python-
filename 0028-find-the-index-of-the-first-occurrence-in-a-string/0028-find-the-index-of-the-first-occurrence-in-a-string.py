class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if needle[0:len(needle)]==haystack[i:i+len(needle)]:
                return i
                exit(0)
        return -1


