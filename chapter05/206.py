class housepark:
    lastname="박"
    def __init__(self,name):
        self.fullname=self.lastname+name
    def travel(self,where):
        print("%s, %s 여행을 가다." % (self.fullname, where))
    def love(self,other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))

class housekim(housepark):
    lastname = '김'
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네." % (self.fullname, where, day))

pey=housepark("응용")
juliet=housekim("줄리엣")
pey.love(juliet)
pey+juliet