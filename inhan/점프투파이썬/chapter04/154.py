a=1
def vartest(a):
#    global a  글로벌 명령어는 a 변수를 직접 사용하겠다. 그러나 사용하지않는 것이 좋다. 함수는 독립적으로 존재하는 것이 좋기 때문에
    a=a+1

vartest(a)
print(a)
#함수만의 변수이기 때문에 1이 나온다.

#def vartest(a):
#    a=a+1
#
#vartest(3)
#print(a) a라는 변수가 없기때문에 오류가 난다.