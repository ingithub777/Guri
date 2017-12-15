while True:
    number = input("숫자를 입력하세요(-1:종료, all:구구단전체출력) : ")
    if number == "-1":
        break

    if number == "all":
        for i in range(2,10):
            for j in range(1,10):
                print("%d * %d = %d" % (i,j,i*j))

    else:
        for i in range(1,10):
            a = int(number) * i
            print("%d * %d = %d" % (int(number), int(i), a))
    break

try:
    number = int(number)
    if number < 0:
        raise ValueError