def mul(num1,num2):
    return num1+num2
def mul(num1, num2, num3):
    return num1+num2+num3
print(mul(1,2,4))

class housepark:
    lastname="박"
    #def setname(self,name): 안된다
    def __init__(self,name):
        self.fullname=self.lastname+name
    def travel(self,where):
        print("%s, %s 여행을 가다." % (self.fullname, where))

pey=housepark("응용")
pey.travel("태국")
#pey.travel("부산")
#pey.setname("응용") 안된다.

class housekim(housepark): #메서드 오버라이딩 - 상속받은걸 다르게 고칠 수 있다.
    lastname="김"
    def travel(self,where, day):
        print("%s, %s 여행을 %d일 가다." % (self.fullname, where, day))

juliet = housekim("줄리엣")
juliet.travel("독도",3)