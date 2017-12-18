while True:
    a = input("두 수를 입력하세요 : ").split(' ')
    for i in (1,16):
        number1 = int(a[0]) * i
        number2 = int(a[1]) * i

    print(number1,number2)