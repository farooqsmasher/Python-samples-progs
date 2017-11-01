
class Democlass:

    def __init__(self):
     self.s= ""

    def read(self):
        self.s = input()

    def prin(self):
        print (self.s.upper())
if __name__ == '__main__':
 obs = Democlass()
 obs.read()
 obs.prin()