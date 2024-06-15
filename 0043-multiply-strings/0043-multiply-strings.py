class Solution(object):
    def multiply(self, num1, num2):
        if num1=='0' or num2=='0':
            return '0'
        def decode(num):
            ans=0
            for i in num:
                ans=ans*10+ord(i)-ord('0')
            return ans
        def encode(num):
            news=''
            while num:
                a=num%10
                num=num//10
                news=chr(ord('0')+a)+news
            return news
        return encode(decode(num1)*decode(num2))
