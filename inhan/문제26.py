while True:
    def sum():
        a = input("두 수를 입력하세요 : ").split(' ')
        a[0] = int(a[0])
        a[1] = int(a[1])
        b = a[0]+a[1]
        print (b)

        try:
            a[0] = int(a[0])
            a[1] = int(a[1])
        except ValueError:
            print("죄송합니다 입력이 %s입니다. 숫자를 입력하세요." % b)
    break
sum()
