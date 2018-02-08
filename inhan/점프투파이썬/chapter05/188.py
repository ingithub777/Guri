class fourcal:
    def setdata(self, first, second):
        self.first = first # 디버그에서 스텝아웃 하려면 f8단축키
        self.second = second
    def sum(self):
         result=self.first+self.second
         return result
        # return self.first+self.second

a = fourcal()
fourcal.setdata(a, 4, 2) # 디버그에서 f7을 누르면 def 함수를 디버그할 수 있다.
# a.setdata(4,2)        이것도 되고 위에것도 되고

print(a.first)
print(a.second)

a.first = 1 # 숫자 수정도 가능하다.
a.second = 2

print(a.first)
print(a.second)

print(a.sum())