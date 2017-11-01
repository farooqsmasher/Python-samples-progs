class Seprator:
    def sepr(self):

        read= input()

        seprate = read.split(":")

        tup = tuple(seprate)

        print(seprate)
        print()
        print(tup)

if __name__ == '__main__':

 obj = Seprator()
 obj.sepr()