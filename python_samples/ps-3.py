import sys
class multiples:


        def mul(self):
            a = int(input())
            d =dict()
            for i in range(a,a+1):
                d[i]=i*i
                print(d)


if __name__ == '__main__':
  t=multiples()
t.mul()