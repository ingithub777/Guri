class service:
    secret = "영구는 배꼽이 두개다."  # sceret = 멤버 변수

    # def setname(self, name):
    def __init__(self, name):
        self.name = name
        print("멤버변수 %s 를 초기화 하였습니다." % self.name)

    def a(self, a, b):  # 멤버함수를 아무렇게나 지정해줘도 된다. (a는 멤버 함수)
        result = a + b  # result는 a의 로컬변수
        print("%s님%s+%s=%s입니다." % (self.name, a, b, result))

    def __del__(self):
        print("저희 서비스를 이용해 주셔서 감사합니다.")


input()
pey = service("홍길동")

input()

pey.a(1, 1)
input()


# pey=service("홍길동") 가능해졌다. ( _init_ 함수덕분에)
# pay=service()
# pey.setname("홍길동")
# pay.setname("김인한") # .setname 쓰나 .name을 쓰나 같은 효과를 가진다.
# pey.name="홍길동"
# pay.name="김인한"
# pey.a(1,1)
# pay.a(1,2)


# secret="영구는 배꼽이 세개다"   중간에 바꾸려고해도 바뀌지않는다.
# print(pey.secret,pay.secret)
