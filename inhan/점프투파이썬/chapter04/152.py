#def say_myself(name,man=True,old): 초기값 설정시 오류사항
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27) #True,False를 입력하지않아도 초기값이 True이기 때문에'남자입니다'가 나온다.
#say_myself("박응용", 27, True)
#say_myself("박응용", 27, False) False를 입력하면 '여자입니다'가 나온다.
#초기값을 설정하지않으면 에러가 뜬다.