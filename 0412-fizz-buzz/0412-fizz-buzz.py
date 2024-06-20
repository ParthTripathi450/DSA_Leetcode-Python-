class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        L=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                L.append('FizzBuzz')
            elif i%5==0:
                L.append('Buzz')
            elif i%3==0:
                L.append('Fizz')
            else:
                i=str(i)
                L.append(i)
        return L