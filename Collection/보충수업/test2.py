number = int(input("숫자를 입력하세요(1,12): "))
if number in range(0,13):
    # print("{0:0=2}".format(number)+"입니다.")
    print(str(number).zfill(2)+"입니다.") # 또 다른 방법 (문자열 포맷팅말구)
else:
    print("정상값이 아닙니다. 1~12 숫자를 입력하세요.")